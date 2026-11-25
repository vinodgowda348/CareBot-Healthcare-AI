# Week 6 Checkpoint 3 – Model Experimentation Report

## Project
CareBot Healthcare AI

## Objective
Train and compare at least two Random Forest hyperparameter configurations using MLflow experiment tracking.

## Dataset and Method
- Dataset: aiml_healthcare_symptoms.csv
- Data split: 70% training, 15% validation, 15% testing
- Random state: 42
- Evaluation metrics: Accuracy and weighted F1-score
- Experiment tracking: MLflow 3.18.0 with SQLite

## Experiment Results

| Configuration | Validation Accuracy | Validation Weighted F1 |
|---|---:|---:|
| 100 trees, unlimited depth | 85.00% | 84.85% |
| 200 trees, max depth 10 | 84.17% | 83.92% |

## Best Configuration
- Model: Random Forest
- n_estimators: 100
- max_depth: None
- random_state: 42

The first configuration achieved the highest validation accuracy and was selected as the best model.

## Final Test Results
- Test Accuracy: 82.50%
- Test Weighted F1-score: 82.37%

## MLflow Experiment Tracking
Experiment name: CareBot-W6-RandomForest

Completed runs:
1. RF_100_depth_None
2. RF_200_depth_10
3. Best_Model_Final_Test

## Conclusion
Two Random Forest configurations were trained and evaluated. The configuration with 100 trees and unlimited depth achieved the best validation performance. The selected model achieved 82.50% test accuracy and 82.37% weighted F1-score on the held-out test set.
