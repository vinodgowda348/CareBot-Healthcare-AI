# CareBot Healthcare AI

## Project Overview

CareBot Healthcare AI is an AI/ML healthcare project designed to process synthetic clinical notes and extract important medical information.

The system extracts:

* Diagnosis
* Medication
* Follow-up information

It then generates a structured patient-record summary.

## Project Objectives

The main objectives of this project are:

1. Process clinical notes written as text.
2. Extract important clinical information.
3. Convert extracted information into structured JSON.
4. Generate a short patient-record summary.
5. Test the pipeline using 30 synthetic clinical notes.
6. Avoid using real patient data.

## Project Structure

```text
CareBot-Healthcare-AI/
├── data/
│   ├── aiml_healthcare_symptoms.csv
│   └── aiml_healthcare_test_cases.txt
├── docs/
├── notebooks/
├── outputs/
│   └── carebot_30_test_results.json
├── src/
│   ├── model.py
│   ├── ner_extraction.py
│   ├── pipeline.py
│   ├── preprocessing.py
│   └── summarization.py
├── tests/
│   ├── test_healthcare_cases.py
│   └── test_30_notes.py
└── README.md
```

## Pipeline

```text
Clinical Note
      ↓
Text Preprocessing
      ↓
Clinical Information Extraction
      ↓
Diagnosis / Medication / Follow-up
      ↓
Structured JSON
      ↓
Patient Record Summary
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Regular Expressions
* JSON
* Healthcare NLP concepts

## Testing

The project includes healthcare test cases covering:

* Pneumonia risk
* Type 2 diabetes
* Hypertension
* Iron deficiency anaemia
* Healthy patient classification
* False-positive prediction
* Model accuracy
* SHAP feature importance
* Dataset splitting
* AUC-ROC evaluation

All 10 healthcare test cases pass successfully.

The project also processes 30 synthetic clinical notes successfully.

## 30-Note Test

The 30-note test processes synthetic clinical notes through the complete pipeline.

The generated structured results are saved as:

```text
outputs/carebot_30_test_results.json
```

Each result contains:

* Test note ID
* Clinical note
* Extracted diagnosis
* Extracted medication
* Follow-up information
* Generated summary

## Example

### Input

```text
Patient has diabetes and hypertension.
Prescribed Metformin 500 mg twice daily.
Follow-up review after two weeks.
```

### Structured Output

```json
{
  "diagnosis": [
    "diabetes",
    "hypertension"
  ],
  "medication": [
    "Metformin 500 mg twice daily"
  ],
  "follow_up": [
    "Follow-up review after two weeks"
  ]
}
```

### Summary

```text
Diagnosis: diabetes, hypertension. Medication: Metformin 500 mg twice daily. Follow-up: Follow-up review after two weeks.
```

## Privacy and Safety

This project uses synthetic test data only.

No real patient information or personally identifiable healthcare data is used.

The system is intended as an AI/ML internship project and is not a replacement for professional medical diagnosis or treatment.

## Project Status

* Clinical information extraction: Completed
* Patient summary generation: Completed
* Healthcare test cases: 10/10 passing
* 30 synthetic clinical notes: Completed
* Structured JSON output: Completed
* GitHub submission: Pending
