from math import radians, sin, cos, sqrt, atan2


def mask_phone(phone: str) -> str:
    """
    Mask donor phone number for privacy.
    Example: 03001234567 -> 0300*****67
    """
    if not phone or len(phone) < 4:
        return "Hidden"

    return phone[:4] + "*****" + phone[-2:]


def mask_name(name: str) -> str:
    """
    Mask donor name for privacy.
    Example: Ahmed Raza -> Ahmed R.
    """
    if not name:
        return "Hidden Donor"

    parts = name.split()

    if len(parts) == 1:
        return parts[0][0] + "***"

    return parts[0] + " " + parts[-1][0] + "."


def calculate_age_score(age: int) -> int:
    """
    Give score based on donor age.
    This is simple MVP logic.
    """
    if 18 <= age <= 40:
        return 15
    elif 41 <= age <= 55:
        return 10
    elif 56 <= age <= 65:
        return 5
    return 0


def calculate_distance_km(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float
) -> float:
    """
    Calculate approximate distance between two coordinates using Haversine formula.
    """
    radius_earth_km = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return round(radius_earth_km * c, 2)


def calculate_distance_score(distance_km: float) -> int:
    """
    Give score based on donor distance.
    Closer donor gets higher score.
    """
    if distance_km <= 5:
        return 20
    elif distance_km <= 15:
        return 15
    elif distance_km <= 30:
        return 10
    elif distance_km <= 50:
        return 5
    return 0


def build_match_reason(
    request_type: str,
    blood_group: str,
    city_match: bool,
    distance_km: float | None,
    urgency: str
) -> str:
    """
    Create a readable explanation for why donor matched.
    """
    reasons = []

    reasons.append(f"Compatible blood group for {blood_group} recipient")

    if request_type == "organ":
        reasons.append("Required organ is available")

    if city_match:
        reasons.append("Donor is located in the same city")

    if distance_km is not None:
        reasons.append(f"Approximate distance is {distance_km} km")

    reasons.append(f"Request urgency level is {urgency}")

    return ". ".join(reasons) + "."