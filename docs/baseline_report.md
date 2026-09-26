# CareBot Healthcare AI — Baseline Model Report

## 1. Objective

The objective of the baseline experiment is to establish an initial machine learning benchmark for healthcare diagnosis classification using the CareBot synthetic healthcare dataset.

## 2. Dataset

The dataset used was:

`data/aiml_healthcare_symptoms.csv`

The `Patient_ID` column was removed because it is an identifier and is not useful for prediction.

The target variable is:

`Diagnosis`

The dataset contains 8 diagnosis classes:

- Anaemia
- Gastroenteritis
- Healthy
- Hypertension
- Influenza
- Migraine
- Pneumonia
- Type2Diabetes

## 3. Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the healthcare dataset using Pandas.
2. Removed the `Patient_ID` column.
3. Separated input features and the `Diagnosis` target.
4. Converted categorical features into numerical features using one-hot encoding.
5. Encoded diagnosis labels using LabelEncoder.
6. Split the dataset using a stratified 70:15:15 train-validation-test split.

## 4. Baseline Model

A Random Forest Classifier was used as the baseline machine learning model.

Configuration:

- Model: RandomForestClassifier
- Number of estimators: 100
- Random state: 42

## 5. Dataset Split

| Dataset | Samples |
|---|---:|
| Training | 560 |
| Validation | 120 |
| Test | 120 |

## 6. Baseline Results

The baseline model achieved:

**Test Accuracy: 0.80 (80%)**

### Classification Results

| Diagnosis | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Anaemia | 0.75 | 0.60 | 0.67 |
| Gastroenteritis | 0.79 | 0.73 | 0.76 |
| Healthy | 0.70 | 0.93 | 0.80 |
| Hypertension | 0.67 | 0.80 | 0.73 |
| Influenza | 0.91 | 0.67 | 0.77 |
| Migraine | 0.67 | 0.67 | 0.67 |
| Pneumonia | 1.00 | 1.00 | 1.00 |
| Type2Diabetes | 1.00 | 1.00 | 1.00 |

## 7. Benchmark

The baseline test accuracy of **80%** will be used as the initial benchmark for future model improvements.

Future experiments can compare new models and preprocessing approaches against this baseline.

## 8. Conclusion

The baseline pipeline successfully loads and preprocesses the healthcare dataset, performs a stratified train-validation-test split, trains a Random Forest classifier, and evaluates its performance.

The baseline model achieved **80% test accuracy**, providing a measurable benchmark for future experimentation.