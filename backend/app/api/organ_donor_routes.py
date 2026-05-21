from fastapi import APIRouter, HTTPException

from app.schemas.organ_donor_schema import OrganDonorCreate
from app.database.supabase_client import supabase


router = APIRouter(
    prefix="/organ-donors",
    tags=["Organ Donors"]
)


@router.post("/")
def create_organ_donor(donor: OrganDonorCreate):
    try:
        response = supabase.table("organ_donors").insert(donor.model_dump()).execute()

        return {
            "message": "Organ donor added successfully",
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
def get_organ_donors():
    try:
        response = supabase.table("organ_donors").select("*").execute()

        return {
            "total": len(response.data),
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))