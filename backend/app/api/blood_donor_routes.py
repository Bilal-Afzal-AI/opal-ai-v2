from fastapi import APIRouter, HTTPException

from app.schemas.blood_donor_schema import BloodDonorCreate
from app.database.supabase_client import supabase


router = APIRouter(
    prefix="/blood-donors",
    tags=["Blood Donors"]
)


@router.post("/")
def create_blood_donor(donor: BloodDonorCreate):
    try:
        response = supabase.table("blood_donors").insert(donor.model_dump()).execute()

        return {
            "message": "Blood donor added successfully",
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
def get_blood_donors():
    try:
        response = supabase.table("blood_donors").select("*").execute()

        return {
            "total": len(response.data),
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))