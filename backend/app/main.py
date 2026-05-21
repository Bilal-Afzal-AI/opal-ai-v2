from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.hospital_routes import router as hospital_router
from app.api.blood_donor_routes import router as blood_donor_router
from app.api.organ_donor_routes import router as organ_donor_router
from app.api.matching_routes import router as matching_router
from app.database.supabase_client import supabase
from app.api.chat_routes import router as chat_router

app = FastAPI(
    title="OPAL-AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
       "http://localhost:3000",
       "http://127.0.0.1:3000",
    "http://192.168.10.2:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hospital_router)
app.include_router(blood_donor_router)
app.include_router(organ_donor_router)
app.include_router(matching_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Welcome to OPAL-AI Backend API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/db-test")
def db_test():
    try:
        response = supabase.table("hospitals").select("*").limit(1).execute()

        return {
            "status": "connected",
            "data": response.data
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }