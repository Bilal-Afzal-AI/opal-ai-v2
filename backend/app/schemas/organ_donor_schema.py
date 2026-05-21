from pydantic import BaseModel
from typing import Optional

class OrganDonorCreate(BaseModel):
    full_name: str
    blood_group: str
    organ: str
    age: int
    city: str
    phone: str
    available: bool = True
    latitude: Optional[float] = None
    longitude: Optional[float] = None