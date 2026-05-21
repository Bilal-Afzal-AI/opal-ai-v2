from pydantic import BaseModel
from typing import Optional

class HospitalCreate(BaseModel):
    name: str
    city: str
    state: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None