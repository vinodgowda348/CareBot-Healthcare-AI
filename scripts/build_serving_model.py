import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/aiml_healthcare_symptoms.csv")
df = df.drop(columns=["Patient_ID"])

X = df.drop(columns=["Diagnosis"])
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df["Diagnosis"])

# Reproduce the Week 6 data split
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

# Apply the same preprocessing as the experiment
X_train = pd.get_dummies(X_train, drop_first=True)
X_val = pd.get_dummies(X_val, drop_first=True)
X_val = X_val.reindex(columns=X_train.columns, fill_value=0)

# Combine training and validation data
X_train_full = pd.concat([X_train, X_val])
y_train_full = list(y_train) + list(y_val)

# Train the selected Week 6 model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train_full, y_train_full)

# Save model and preprocessing information
os.makedirs("models", exist_ok=True)

artifact = {
    "model": model,
    "feature_columns": list(X_train.columns),
    "diagnosis_classes": list(label_encoder.classes_)
}

joblib.dump(artifact, "models/carebot_model.joblib")

print("CAREBOT SERVING MODEL CREATED")
print("Model: Random Forest")
print("Trees: 100")
print("Training records:", len(X_train_full))
print("Features:", len(X_train.columns))
print("Diagnosis classes:", list(label_encoder.classes_))
print("Saved: models/carebot_model.joblib")
