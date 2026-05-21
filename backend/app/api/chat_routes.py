from fastapi import APIRouter, HTTPException

from app.schemas.chat_schema import ChatRequest
from app.services.gemini_service import generate_chat_response

router = APIRouter(
    prefix="/chat",
    tags=["AI Chatbot"]
)


@router.post("/")
def chat_with_ai(request: ChatRequest):
    try:
        ai_response = generate_chat_response(
            message=request.message,
            role=request.role
        )

        return {
            "user_message": request.message,
            "role": request.role,
            "response": ai_response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))