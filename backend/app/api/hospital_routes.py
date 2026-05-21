from fastapi import APIRouter, HTTPException

from app.schemas.hospital_schema import HospitalCreate
from app.database.supabase_client import supabase


router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)


@router.post("/")
def create_hospital(hospital: HospitalCreate):
    try:
        response = supabase.table("hospitals").insert(hospital.model_dump()).execute()

        return {
            "message": "Hospital created successfully",
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
def get_hospitals():
    try:
        response = supabase.table("hospitals").select("*").execute()

        return {
            "total": len(response.data),
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))