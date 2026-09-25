def clean_text(text):
    """
    Clean a clinical note by removing extra spaces.
    """
    text = text.strip()
    text = " ".join(text.split())
    return text


def preprocess_notes(notes):
    """
    Preprocess a list of clinical notes.
    """
    return [clean_text(note) for note in notes]