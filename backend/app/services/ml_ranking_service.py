import os
import joblib
import pandas as pd


MODEL_PATH = "app/ml/models/donor_ranking_model.pkl"


def load_model():
    """
    Load trained donor ranking ML model.
    """
    if not os.path.exists(MODEL_PATH):
        return None

    return joblib.load(MODEL_PATH)


model = load_model()


def urgency_to_score(urgency: str) -> int:
    """
    Convert urgency text into numeric ML feature.
    """
    urgency = urgency.lower()

    if urgency == "high":
        return 3
    if urgency == "medium":
        return 2
    return 1


def predict_ml_score(
    donor_age: int,
    urgency: str,
    distance_km: float | None,
    same_city: bool,
    available: bool,
    blood_compatible: bool,
) -> float:
    """
    Predict donor suitability score using ML model.
    Falls back to rule-like score if model is missing.
    """

    if distance_km is None:
        distance_km = 100.0

    features = pd.DataFrame(
        [
            {
                "donor_age": donor_age,
                "urgency_score": urgency_to_score(urgency),
                "distance_km": distance_km,
                "same_city": 1 if same_city else 0,
                "available": 1 if available else 0,
                "blood_compatible": 1 if blood_compatible else 0,
            }
        ]
    )

    if model is None:
        fallback_score = 0

        if blood_compatible:
            fallback_score += 40

        if available:
            fallback_score += 20

        if same_city:
            fallback_score += 15

        if donor_age < 40:
            fallback_score += 10

        if distance_km < 50:
            fallback_score += 10

        fallback_score += urgency_to_score(urgency) * 5

        return min(float(fallback_score), 100.0)

    prediction = model.predict(features)[0]

    return round(float(max(0, min(prediction, 100))), 2)