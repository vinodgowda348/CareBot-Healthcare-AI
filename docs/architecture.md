# CareBot Healthcare AI - System Architecture

## 1. Overview

CareBot is an AI-powered clinical note processing system.
It processes synthetic doctor-patient clinical notes and
extracts important medical information.

## 2. System Components

### Component 1: Input
Accepts clinical notes as text transcripts.

### Component 2: Text Preprocessing
Cleans and prepares clinical text for processing.

### Component 3: Clinical Information Extraction
Uses custom Named Entity Recognition (NER) and
extraction rules to identify:
- Diagnosis
- Medication
- Follow-up

### Component 4: LLM Summarization
Uses a language model to generate concise summaries
without inventing information.

### Component 5: Structured Output
Converts extracted information into JSON format.

### Component 6: Testing
Evaluates the pipeline using 30 synthetic clinical notes.

## 3. Architecture Flow

Clinical Notes
      |
      v
Text Preprocessing
      |
      v
Custom NER and Information Extraction
      |
      v
Diagnosis / Medication / Follow-up
      |
      v
LLM Summarization
      |
      v
Structured JSON + Summary Paragraph
      |
      v
Testing and Evaluation

## 4. Technologies

- Python
- spaCy
- Regular Expressions
- Ollama
- Llama 3.2
- JSON
- Pandas
- Scikit-learn

## 5. Data Privacy

Only synthetic clinical notes are used.
No real patient information is processed.

## 6. Limitations

This system is an internship prototype.
It does not replace professional medical
judgment, diagnosis or treatment.
