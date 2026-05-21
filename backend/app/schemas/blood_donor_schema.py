from pydantic import BaseModel
from typing import Optional

class BloodDonorCreate(BaseModel):
    full_name: str
    blood_group: str
    age: int
    city: str
    phone: str
    available: bool = True
    latitude: Optional[float] = None
    longitude: Optional[float] = None