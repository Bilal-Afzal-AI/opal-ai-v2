from google import genai
from app.core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def fallback_response(message: str) -> str:
    """
    Local fallback response when Gemini quota/API fails.
    This keeps the chatbot usable during demos.
    """

    message_lower = message.lower()

    if "a+" in message_lower or "blood" in message_lower:
        return (
            "For blood group A+, a recipient can usually receive blood from "
            "A+, A-, O+, and O- donors. OPAL-AI checks this compatibility first, "
            "then combines urgency, donor availability, age, city, and distance "
            "to calculate a match score. Final medical verification must always "
            "be done by hospital professionals."
        )

    if "urgency" in message_lower:
        return (
            "Urgency affects the match score by giving higher priority to critical "
            "requests. In OPAL-AI, high urgency receives a stronger score boost than "
            "medium or low urgency so emergency cases appear higher in matching results."
        )

    if "score" in message_lower or "match" in message_lower:
        return (
            "The OPAL-AI match score is calculated using compatibility, urgency, "
            "donor age, city match, distance, and availability. A higher score means "
            "the donor is more suitable based on the system rules, but final decisions "
            "should be reviewed by clinical staff."
        )

    if "organ" in message_lower or "kidney" in message_lower:
        return (
            "For organ matching, OPAL-AI checks whether the donor has the required organ, "
            "whether the blood group is compatible, whether the donor is available, and "
            "how close the donor is to the hospital or recipient location."
        )

    return (
        "OPAL-AI helps hospitals search and rank compatible blood or organ donors. "
        "It uses clinical compatibility rules, urgency, donor availability, distance, "
        "and AI-assisted explanations. This is a decision-support tool, not a replacement "
        "for clinical judgment."
    )


def generate_chat_response(message: str, role: str = "hospital_staff") -> str:
    system_context = f"""
You are OPAL-AI, an AI assistant for a clinical donor matching platform.

User role: {role}

You can help with:
- explaining blood donor matching
- explaining organ donor matching
- explaining urgency and compatibility
- explaining how to use the OPAL-AI dashboard
- giving safe, general healthcare workflow information

Important safety rules:
- Do not give final medical decisions.
- Do not replace doctors or clinical experts.
- Always recommend hospital/clinical verification for real patient decisions.
- Keep answers simple, clear, and professional.
"""

    prompt = f"""
{system_context}

User question:
{message}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        return response.text or fallback_response(message)

    except Exception:
        return fallback_response(message)