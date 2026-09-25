def create_summary(extracted_data):
    """
    Create a simple patient-record summary
    from extracted clinical information.
    """

    diagnosis = extracted_data.get("diagnosis", [])
    medication = extracted_data.get("medication", [])
    follow_up = extracted_data.get("follow_up", [])

    parts = []

    if diagnosis:
        parts.append("Diagnosis: " + ", ".join(diagnosis))

    if medication:
        parts.append("Medication: " + ", ".join(medication))

    if follow_up:
        parts.append("Follow-up: " + ", ".join(follow_up))

    return ". ".join(parts) + "." if parts else "No clinical information extracted."