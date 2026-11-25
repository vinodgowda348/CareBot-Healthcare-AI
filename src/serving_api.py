import joblib
import pandas as pd

from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "carebot_model.joblib"

artifact = joblib.load(MODEL_PATH)
model = artifact["model"]
feature_columns = artifact["feature_columns"]
diagnosis_classes = artifact["diagnosis_classes"]

app = FastAPI(
    title="CareBot Healthcare AI API",
    description="Educational healthcare dataset prediction API",
    version="1.0.0"
)


class PatientInput(BaseModel):
    Age: int = Field(ge=0, le=120)
    Gender: str
    Fever: int = Field(ge=0, le=1)
    Cough: int = Field(ge=0, le=1)
    Fatigue: int = Field(ge=0, le=1)
    Breathlessness: int = Field(ge=0, le=1)
    Chest_Pain: int = Field(ge=0, le=1)
    Nausea: int = Field(ge=0, le=1)
    Headache: int = Field(ge=0, le=1)
    BMI: float = Field(gt=0, le=100)
    BP_Systolic: int = Field(gt=0, le=300)
    BP_Diastolic: int = Field(gt=0, le=200)
    SpO2: int = Field(ge=0, le=100)
    Glucose_mg_dL: int = Field(gt=0, le=1000)
    HbA1c: float = Field(ge=0, le=30)


@app.get("/")
def home():
    return {
        "message": "CareBot Healthcare AI API is running",
        "model": "Random Forest",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict")
def predict(patient: PatientInput):
    try:
        patient_data = patient.model_dump()

        gender = patient_data.pop("Gender")
        input_df = pd.DataFrame([patient_data])
        input_df["Gender"] = gender

        input_df = pd.get_dummies(input_df, drop_first=True)
        input_df = input_df.reindex(
            columns=feature_columns,
            fill_value=0
        )

        prediction = int(model.predict(input_df)[0])
        probabilities = model.predict_proba(input_df)[0]

        return {
            "prediction": diagnosis_classes[prediction],
            "model": "Random Forest",
            "confidence": round(float(max(probabilities)), 4),
            "notice": "Educational prediction only; not a medical diagnosis."
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction could not be completed."
        ) from exc
