from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    role: str = "hospital_staff"


class ChatResponse(BaseModel):
    response: str