import random
import pandas as pd


blood_groups = [
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
    "O+",
    "O-"
]

urgency_levels = ["low", "medium", "high"]

cities = [
    "Lahore",
    "Karachi",
    "Islamabad",
    "Faisalabad",
    "Rawalpindi"
]


def generate_row():
    donor_age = random.randint(18, 60)

    urgency = random.choice(urgency_levels)

    distance_km = round(random.uniform(1, 500), 2)

    same_city = random.choice([0, 1])

    available = random.choice([0, 1])

    blood_compatible = random.choice([0, 1])

    if urgency == "low":
        urgency_score = 1
    elif urgency == "medium":
        urgency_score = 2
    else:
        urgency_score = 3

    score = 0

    if blood_compatible:
        score += 40

    if available:
        score += 20

    if same_city:
        score += 15

    if donor_age < 40:
        score += 10

    if distance_km < 50:
        score += 10

    score += urgency_score * 5

    score += random.randint(-5, 5)

    score = max(0, min(score, 100))

    return {
        "donor_age": donor_age,
        "urgency_score": urgency_score,
        "distance_km": distance_km,
        "same_city": same_city,
        "available": available,
        "blood_compatible": blood_compatible,
        "match_score": score
    }


data = [generate_row() for _ in range(2000)]

df = pd.DataFrame(data)

output_path = "app/ml/data/training_data.csv"

df.to_csv(output_path, index=False)

print(f"Training dataset saved to: {output_path}")
print(df.head())
