# CareBot Healthcare AI - Literature Review

## 1. BioBERT: A Pre-trained Biomedical Language Representation Model

Authors: Jinhyuk Lee et al.
Published: 2020
Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC7703786/

### Research Summary
This research introduces BioBERT, a language representation model
pre-trained using biomedical text. It improves biomedical
named entity recognition, relation extraction and question answering.

### Relevance to CareBot
The research helps explain why domain-specific NLP is useful
for identifying medical terminology in clinical notes.

## 2. Adapted Large Language Models for Clinical Text Summarization

Authors: Dave Van Veen et al.
Published: 2024
Link: https://www.nature.com/articles/s41591-024-02855-5

### Research Summary
This research evaluates large language models across different
clinical summarization tasks, including progress notes and
doctor-patient dialogue.

It evaluates summary completeness, correctness and conciseness.

### Relevance to CareBot
It provides research support for using language models to
generate concise clinical summaries while checking factual accuracy.

## 3. spaCy Rule-Based Matching and EntityRuler

Source: spaCy Official Documentation
Link: https://spacy.io/usage/rule-based-matching/

### Research Summary
spaCy provides rule-based matching tools to identify phrases
and named entities using token patterns and phrase patterns.
EntityRuler can be combined with statistical NER models.

### Relevance to CareBot
This approach is useful for creating custom extraction rules
for diagnosis, medication and follow-up information.

## 4. Literature Review Findings

The reviewed sources support three important components:

1. Biomedical NLP helps process medical terminology.
2. Language models can generate clinical text summaries.
3. Rule-based entity recognition can extract structured information.

These findings inform the proposed CareBot architecture.

## 5. Conclusion

CareBot combines text preprocessing, custom clinical information
extraction, structured JSON generation and clinical note summarization.

The system is evaluated using synthetic clinical notes only.
No real patient information is used.
