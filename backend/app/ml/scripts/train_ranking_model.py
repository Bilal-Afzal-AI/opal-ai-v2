import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

import joblib


# Load dataset
data_path = "app/ml/data/training_data.csv"

df = pd.read_csv(data_path)

print("Dataset loaded successfully")
print(df.head())


# Features
X = df[
    [
        "donor_age",
        "urgency_score",
        "distance_km",
        "same_city",
        "available",
        "blood_compatible"
    ]
]

# Target
y = df["match_score"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)

print("Model training completed")


# Predictions
predictions = model.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")

print(f"R2 Score: {r2:.2f}")


# Save model
model_output_path = "app/ml/models/donor_ranking_model.pkl"

joblib.dump(model, model_output_path)

print(f"Model saved to: {model_output_path}")