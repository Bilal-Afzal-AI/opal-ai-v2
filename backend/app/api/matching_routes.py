from app.services.ml_ranking_service import predict_ml_score
from fastapi import APIRouter, HTTPException

from app.schemas.match_schema import MatchRequest
from app.database.supabase_client import supabase
from app.utils.matching_utils import (
    mask_name,
    mask_phone,
    calculate_age_score,
    calculate_distance_km,
    calculate_distance_score,
    build_match_reason,
)


router = APIRouter(
    prefix="/matching",
    tags=["Matching"]
)


def is_blood_compatible(recipient_blood: str, donor_blood: str) -> bool:
    compatibility = {
        "A+": ["A+", "A-", "O+", "O-"],
        "A-": ["A-", "O-"],
        "B+": ["B+", "B-", "O+", "O-"],
        "B-": ["B-", "O-"],
        "AB+": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
        "AB-": ["A-", "B-", "AB-", "O-"],
        "O+": ["O+", "O-"],
        "O-": ["O-"],
    }

    return donor_blood.upper() in compatibility.get(recipient_blood.upper(), [])


def urgency_score(urgency: str) -> int:
    urgency = urgency.lower()

    if urgency == "high":
        return 30
    if urgency == "medium":
        return 20
    return 10


def calculate_match_score(
    donor: dict,
    request: MatchRequest,
    distance_km: float | None
) -> int:
    score = 40

    if donor.get("city", "").lower() == request.city.lower():
        score += 15

    score += urgency_score(request.urgency)
    score += calculate_age_score(donor.get("age", 0))

    if distance_km is not None:
        score += calculate_distance_score(distance_km)

    return min(score, 100)


def get_distance_if_available(donor: dict, request: MatchRequest) -> float | None:
    donor_lat = donor.get("latitude")
    donor_lon = donor.get("longitude")

    if (
        donor_lat is None
        or donor_lon is None
        or request.latitude is None
        or request.longitude is None
    ):
        return None

    return calculate_distance_km(
        request.latitude,
        request.longitude,
        donor_lat,
        donor_lon
    )


def already_added(matches: list, donor_name: str, phone: str) -> bool:
    for match in matches:
        if match.get("original_name") == donor_name and match.get("original_phone") == phone:
            return True

    return False


@router.post("/find")
def find_matches(request: MatchRequest):
    if request.request_type.lower() not in ["blood", "organ"]:
        raise HTTPException(
            status_code=400,
            detail="request_type must be either 'blood' or 'organ'"
        )

    # Save match request to Supabase
    supabase.table("match_requests").insert(request.model_dump()).execute()

    matches = []

    if request.request_type.lower() == "blood":
        response = supabase.table("blood_donors").select("*").execute()
        donor_list = response.data
    else:
        response = supabase.table("organ_donors").select("*").execute()
        donor_list = response.data

    if request.request_type.lower() == "organ" and not request.organ:
        raise HTTPException(
            status_code=400,
            detail="organ is required when request_type is 'organ'"
        )

    for donor in donor_list:
        if not donor.get("available", False):
            continue

        donor_age = donor.get("age", 0)
        if donor_age < 18 or donor_age > 65:
            continue

        if request.request_type.lower() == "organ":
            if donor.get("organ", "").lower() != request.organ.lower():
                continue

        if not is_blood_compatible(request.blood_group, donor.get("blood_group", "")):
            continue

        if already_added(matches, donor.get("full_name"), donor.get("phone")):
            continue

        distance_km = get_distance_if_available(donor, request)

        city_match = donor.get("city", "").lower() == request.city.lower()

        rule_score = calculate_match_score(donor, request, distance_km)

        ml_score = predict_ml_score(
          donor_age=donor.get("age", 0),
          urgency=request.urgency,
          distance_km=distance_km,
          same_city=city_match,
          available=donor.get("available", False),
          blood_compatible=True,
        )

        final_score = round((rule_score * 0.6) + (ml_score * 0.4), 2)

        match_result = {
            "donor_name": mask_name(donor.get("full_name")),
            "blood_group": donor.get("blood_group"),
            "city": donor.get("city"),
            "phone": mask_phone(donor.get("phone")),
            "age": donor.get("age"),
            "rule_score": rule_score,
            "ml_score": ml_score,
            "match_score": final_score,
            "distance_km": distance_km,
            "reason": build_match_reason(
                request_type=request.request_type.lower(),
                blood_group=request.blood_group,
                city_match=city_match,
                distance_km=distance_km,
                urgency=request.urgency
            ),
            "original_name": donor.get("full_name"),
            "original_phone": donor.get("phone"),
        }

        if request.request_type.lower() == "organ":
            match_result["organ"] = donor.get("organ")

        matches.append(match_result)

    matches = sorted(matches, key=lambda x: x["match_score"], reverse=True)

    for match in matches:
        match.pop("original_name", None)
        match.pop("original_phone", None)

    return {
        "recipient": request.recipient_name,
        "request_type": request.request_type,
        "total_matches": len(matches),
        "matches": matches
    }


@router.get("/requests")
def get_match_requests():
    try:
        response = (
            supabase
            .table("match_requests")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        return {
            "total": len(response.data),
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))