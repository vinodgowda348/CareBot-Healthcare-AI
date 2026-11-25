# CareBot Healthcare AI - Evaluation Metrics

## 1. Introduction

This document defines the evaluation methods used
to assess the CareBot Healthcare AI pipeline.

The project uses synthetic clinical notes only.

## 2. Information Extraction Metrics

The following metrics are used to evaluate
clinical information extraction.

### Precision

Precision measures how many extracted entities
are correct.

Precision = True Positives / (True Positives + False Positives)

### Recall

Recall measures how many relevant entities
were successfully extracted.

Recall = True Positives / (True Positives + False Negatives)

### F1-Score

F1-score is the harmonic mean of precision and recall.

F1-Score = 2 * (Precision * Recall) / (Precision + Recall)

These metrics will be evaluated separately for:
- Diagnosis
- Medication
- Follow-up

## 3. Classification Metrics

The baseline classification model is evaluated
using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

These metrics help assess the classification
performance of the baseline model.

## 4. Summarization Evaluation

Generated clinical summaries are assessed using:

1. Factual consistency:
   Whether the summary preserves the input facts.

2. Completeness:
   Whether important clinical information is retained.

3. Conciseness:
   Whether the summary avoids unnecessary information.

4. Structured output validity:
   Whether generated JSON follows the expected format.

## 5. Testing Strategy

The pipeline is tested using 30 synthetic clinical notes.

Testing checks:
- Diagnosis extraction
- Medication extraction
- Follow-up extraction
- JSON output structure
- Summary generation
- Missing information handling

## 6. Privacy and Safety

Only synthetic data is used for evaluation.

The system is a prototype and is not intended
to replace professional medical judgment.

## 7. Conclusion

Multiple evaluation methods are necessary to
assess clinical information extraction,
classification performance and summary quality.

The results should be documented after testing.
