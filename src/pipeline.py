from preprocessing import clean_text
from ner_extraction import extract_information
from summarization import create_summary


def run_pipeline(note):
    # Step 1: Clean the clinical note
    cleaned_note = clean_text(note)

    # Step 2: Extract clinical information
    extracted_data = extract_information(cleaned_note)

    # Step 3: Create a patient-record summary
    summary = create_summary(extracted_data)

    return {
        "extracted_data": extracted_data,
        "summary": summary
    }


if __name__ == "__main__":
    sample_note = (
        "Patient has diabetes and hypertension. "
        "Prescribed Metformin 500 mg twice daily. "
        "Follow-up review after two weeks."
    )

    result = run_pipeline(sample_note)

    print("=== Extracted Information ===")
    print(result["extracted_data"])

    print("\n=== Patient Summary ===")
    print(result["summary"])