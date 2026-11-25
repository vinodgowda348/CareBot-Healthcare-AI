import os
import json
import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# 1. Load dataset
DATA_PATH = "data/aiml_healthcare_symptoms.csv"
df = pd.read_csv(DATA_PATH)

df = df.drop(columns=["Patient_ID"])

X = df.drop(columns=["Diagnosis"])
y = LabelEncoder().fit_transform(df["Diagnosis"])

# 2. Split into train, validation and test
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

# 3. Encode features consistently
X_train = pd.get_dummies(X_train, drop_first=True)
X_val = pd.get_dummies(X_val, drop_first=True)
X_test = pd.get_dummies(X_test, drop_first=True)

X_val = X_val.reindex(columns=X_train.columns, fill_value=0)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# 4. Configure MLflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("CareBot-W6-RandomForest")

configurations = [
    {"n_estimators": 100, "max_depth": None},
    {"n_estimators": 200, "max_depth": 10},
]

results = []

print("CAREBOT WEEK 6 EXPERIMENTS")
print("Training records:", len(X_train))
print("Validation records:", len(X_val))
print("Test records:", len(X_test))

# 5. Train and compare configurations
for config in configurations:
    model = RandomForestClassifier(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"],
        random_state=42,
        n_jobs=-1
    )

    with mlflow.start_run(run_name=f"RF_{config['n_estimators']}_depth_{config['max_depth']}"):
        model.fit(X_train, y_train)

        predictions = model.predict(X_val)

        val_accuracy = accuracy_score(y_val, predictions)
        val_f1 = f1_score(y_val, predictions, average="weighted")

        mlflow.log_params(config)
        mlflow.log_metric("validation_accuracy", val_accuracy)
        mlflow.log_metric("validation_f1_weighted", val_f1)

        results.append({
            "n_estimators": config["n_estimators"],
            "max_depth": str(config["max_depth"]),
            "validation_accuracy": val_accuracy,
            "validation_f1_weighted": val_f1
        })

        print("\nConfiguration:", config)
        print("Validation accuracy:", round(val_accuracy, 4))
        print("Validation F1:", round(val_f1, 4))

# 6. Select best configuration using validation accuracy
best_result = max(results, key=lambda item: item["validation_accuracy"])

best_config = {
    "n_estimators": best_result["n_estimators"],
    "max_depth": None if best_result["max_depth"] == "None"
    else int(best_result["max_depth"]),
    "random_state": 42
}

print("\nBEST CONFIGURATION:", best_config)

# 7. Retrain best model using training + validation data
X_train_full = pd.concat([X_train, X_val])
y_train_full = list(y_train) + list(y_val)

best_model = RandomForestClassifier(**best_config, n_jobs=-1)
best_model.fit(X_train_full, y_train_full)

# 8. Final evaluation on untouched test data
test_predictions = best_model.predict(X_test)

test_accuracy = accuracy_score(y_test, test_predictions)
test_f1 = f1_score(y_test, test_predictions, average="weighted")

print("\nFINAL TEST RESULTS")
print("Test accuracy:", round(test_accuracy, 4))
print("Test F1:", round(test_f1, 4))
print("\nClassification report:")
print(classification_report(y_test, test_predictions, zero_division=0))

# 9. Save evidence
os.makedirs("outputs", exist_ok=True)

results_df = pd.DataFrame(results)
results_df.to_csv("outputs/w6_experiment_results.csv", index=False)

report = {
    "best_configuration": best_config,
    "selection_metric": "validation_accuracy",
    "validation_accuracy": best_result["validation_accuracy"],
    "validation_f1_weighted": best_result["validation_f1_weighted"],
    "final_test_accuracy": test_accuracy,
    "final_test_f1_weighted": test_f1,
    "training_records": len(X_train),
    "validation_records": len(X_val),
    "test_records": len(X_test)
}

with open("outputs/w6_best_model_report.json", "w") as file:
    json.dump(report, file, indent=4)

# 10. Log final model evidence in MLflow
with mlflow.start_run(run_name="Best_Model_Final_Test"):
    mlflow.log_params(best_config)
    mlflow.log_metric("final_test_accuracy", test_accuracy)
    mlflow.log_metric("final_test_f1_weighted", test_f1)
    mlflow.log_artifact("outputs/w6_experiment_results.csv")
    mlflow.log_artifact("outputs/w6_best_model_report.json")

print("\nExperiment results saved in outputs/")
print("MLflow tracking data saved in mlruns/")
print("\nWEEK 6 EXPERIMENTS COMPLETED")
