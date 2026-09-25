import re


def extract_information(text):
    """
    Extract basic clinical information from a synthetic clinical note.
    """

    result = {
        "diagnosis": [],
        "medication": [],
        "follow_up": []
    }

    text_lower = text.lower()

    # Medication extraction
    medication_pattern = (
        r"\b(?:Metformin|Paracetamol|Amoxicillin|Ibuprofen|"
        r"Amlodipine|Losartan|Telmisartan|Salbutamol|"
        r"iron tablets|iron supplementation)\b[^.,;]*"
    )

    medications = re.findall(
        medication_pattern,
        text,
        re.IGNORECASE
    )

    result["medication"] = [m.strip() for m in medications]

    # Follow-up extraction
    follow_up_pattern = r"(?:follow[- ]?up|review)[^.;]*"

    follow_ups = re.findall(
        follow_up_pattern,
        text,
        re.IGNORECASE
    )

    result["follow_up"] = [f.strip() for f in follow_ups]

    # Diagnosis extraction
    diagnosis_patterns = [
        ("diabetes", [
            "diabetes",
            "high blood glucose",
            "elevated blood glucose",
            "elevated glucose"
        ]),

        ("hypertension", [
            "hypertension",
            "high blood pressure"
        ]),

        ("asthma", [
            "asthma"
        ]),

        ("fever", [
            "fever"
        ]),

        ("anaemia", [
            "anaemia",
            "anemia",
            "iron deficiency anaemia",
            "iron deficiency anemia"
        ]),

        ("infection", [
            "infection"
        ])
    ]

    for diagnosis, keywords in diagnosis_patterns:
        for keyword in keywords:
            if keyword in text_lower:
                result["diagnosis"].append(diagnosis)
                break

    return result