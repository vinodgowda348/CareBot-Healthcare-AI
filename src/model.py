import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv("../data/aiml_healthcare_symptoms.csv")

print("=== DATASET ===")
print("Total records:", len(df))
print("Total columns:", len(df.columns))


# ============================================================
# 2. PREPARE DATA
# ============================================================

# Patient_ID is only an identifier, so remove it
df = df.drop(columns=["Patient_ID"])

# Convert Gender into numbers
gender_encoder = LabelEncoder()
df["Gender"] = gender_encoder.fit_transform(df["Gender"])

# Convert Diagnosis into numbers
diagnosis_encoder = LabelEncoder()
df["Diagnosis"] = diagnosis_encoder.fit_transform(df["Diagnosis"])


# Features (input)
X = df.drop(columns=["Diagnosis"])

# Target (what the model predicts)
y = df["Diagnosis"]


# ============================================================
# 3. TRAIN / VALIDATION / TEST SPLIT
# ============================================================

# First: 70% train, 30% temporary
X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Second: divide temporary 30% into 15% validation and 15% test
X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.50,
    random_state=42,
    stratify=y_temp
)

print("\n=== DATA SPLIT ===")
print("Training records:", len(X_train))
print("Validation records:", len(X_val))
print("Test records:", len(X_test))


# ============================================================
# 4. TRAIN MODEL
# ============================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ============================================================
# 5. VALIDATION
# ============================================================

val_predictions = model.predict(X_val)

val_accuracy = accuracy_score(y_val, val_predictions)

print("\n=== VALIDATION RESULTS ===")
print("Validation accuracy:", round(val_accuracy, 4))


# ============================================================
# 6. FINAL TEST
# ============================================================

test_predictions = model.predict(X_test)

test_accuracy = accuracy_score(y_test, test_predictions)

print("\n=== TEST RESULTS ===")
print("Test accuracy:", round(test_accuracy, 4))

print("\n=== CLASSIFICATION REPORT ===")

print(
    classification_report(
        y_test,
        test_predictions,
        target_names=diagnosis_encoder.classes_
    )
)


# ============================================================
# 7. CONFUSION MATRIX
# ============================================================

print("\n=== CONFUSION MATRIX ===")

print(
    confusion_matrix(
        y_test,
        test_predictions
    )
)


# ============================================================
# 8. FEATURE IMPORTANCE
# ============================================================

print("\n=== FEATURE IMPORTANCE ===")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance.to_string(index=False))