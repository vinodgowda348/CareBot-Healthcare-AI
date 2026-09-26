import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score


# 1. Load healthcare dataset
df = pd.read_csv("data/aiml_healthcare_symptoms.csv")

# 2. Remove Patient ID
df = df.drop(columns=["Patient_ID"])

# 3. Separate features and target
X = df.drop(columns=["Diagnosis"])
y = df["Diagnosis"]

# 4. Convert categorical columns to numbers
X = pd.get_dummies(X, drop_first=True)

# 5. Encode target labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# 6. Split data: 70% train, 15% validation, 15% test
X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.50,
    random_state=42,
    stratify=y_temp
)

# 7. Train baseline model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# 8. Make predictions
y_pred = model.predict(X_test)

# 9. Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("=== CAREBOT BASELINE MODEL ===")
print("Training samples:", len(X_train))
print("Validation samples:", len(X_val))
print("Test samples:", len(X_test))

print("\nBaseline Accuracy:", round(accuracy, 4))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=label_encoder.classes_
))