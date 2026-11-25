from fastapi.testclient import TestClient
from src.serving_api import app

client = TestClient(app)

SAMPLE_INPUT = {
    "Age": 45,
    "Gender": "M",
    "Fever": 1,
    "Cough": 1,
    "Fatigue": 1,
    "Breathlessness": 0,
    "Chest_Pain": 0,
    "Nausea": 0,
    "Headache": 1,
    "BMI": 24.5,
    "BP_Systolic": 120,
    "BP_Diastolic": 80,
    "SpO2": 98,
    "Glucose_mg_dL": 95,
    "HbA1c": 5.4
}

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["model"] == "Random Forest"

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_prediction_endpoint():
    response = client.post("/predict", json=SAMPLE_INPUT)
    assert response.status_code == 200
    result = response.json()
    assert result["prediction"] in [
        "Anaemia", "Gastroenteritis", "Healthy",
        "Hypertension", "Influenza", "Migraine",
        "Pneumonia", "Type2Diabetes"
    ]
    assert 0 <= result["confidence"] <= 1

def test_invalid_input():
    invalid_input = SAMPLE_INPUT.copy()
    invalid_input["Age"] = -5
    response = client.post("/predict", json=invalid_input)
    assert response.status_code == 422
