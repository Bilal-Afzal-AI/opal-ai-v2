from pydantic import BaseModel
from typing import Optional


class MatchRequest(BaseModel):
    recipient_name: str
    blood_group: str
    request_type: str  # "blood" or "organ"
    organ: Optional[str] = None
    city: str
    urgency: str = "medium"  # low, medium, high

    # Optional recipient location
    latitude: Optional[float] = None
    longitude: Optional[float] = None