
import json
import os
import sys

import pytest

# Allow Python to import files from src/
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

from pipeline import run_pipeline


@pytest.fixture(scope="module")
def clinical_notes():
    return [
        "Patient has diabetes. Prescribed Metformin 500 mg twice daily. Follow-up after two weeks.",
        "Patient has hypertension. Prescribed Amlodipine 5 mg once daily. Review after one month.",
        "Patient has fever and cough. Advised rest and fluids. Follow-up after three days.",
        "Patient has asthma with breathing difficulty. Prescribed inhaler. Review after one week.",
        "Patient has high blood pressure. Prescribed Losartan 50 mg once daily. Follow-up after two weeks.",
        "Patient has type 2 diabetes. Taking Metformin 500 mg daily. Review blood glucose after one month.",
        "Patient reports headache and hypertension. Continue medication. Follow-up after two weeks.",
        "Patient has anaemia and fatigue. Recommended iron supplementation. Review after four weeks.",
        "Patient has cough and fever. Advised clinical review after three days.",
        "Patient has diabetes and hypertension. Continue current medications. Follow-up after one month.",
        "Patient has mild asthma. Prescribed Salbutamol inhaler. Review after one week.",
        "Patient has elevated glucose levels. Recommended dietary monitoring. Follow-up after two weeks.",
        "Patient has hypertension. Prescribed Telmisartan 40 mg once daily. Review after one month.",
        "Patient has iron deficiency anaemia. Prescribed iron tablets. Follow-up after four weeks.",
        "Patient has fever with cough. Advised hydration and rest. Review after three days.",
        "Patient has diabetes. Prescribed Metformin 500 mg twice daily. Follow-up after two weeks.",
        "Patient has high blood pressure and headache. Continue medication. Review after one week.",
        "Patient has asthma symptoms. Continue inhaler treatment. Follow-up after two weeks.",
        "Patient has fatigue due to anaemia. Recommended iron supplementation. Review after four weeks.",
        "Patient has hypertension. Continue Amlodipine 5 mg daily. Follow-up after one month.",
        "Patient has diabetes. Continue Metformin treatment. Review glucose after two weeks.",
        "Patient has cough and fever. Advised rest and fluids. Follow-up after three days.",
        "Patient has asthma. Prescribed inhaler and advised monitoring. Review after one week.",
        "Patient has anaemia. Prescribed iron supplementation. Follow-up after four weeks.",
        "Patient has hypertension. Prescribed Losartan 50 mg daily. Review after one month.",
        "Patient has diabetes and hypertension. Continue current treatment. Follow-up after two weeks.",
        "Patient has elevated blood glucose. Continue monitoring. Review after one month.",
        "Patient has fever and cough. Advised rest and hydration. Follow-up after three days.",
        "Patient has iron deficiency anaemia with fatigue. Continue iron treatment. Review after four weeks.",
        "Patient has diabetes. Prescribed Metformin 500 mg twice daily. Follow-up after two weeks."
    ]


def test_exactly_30_clinical_notes(clinical_notes):
    assert len(clinical_notes) == 30


def test_pipeline_returns_expected_fields(clinical_notes):
    result = run_pipeline(clinical_notes[0])

    assert "extracted_data" in result
    assert "summary" in result


def test_diagnosis_extraction(clinical_notes):
    result = run_pipeline(clinical_notes[0])

    assert "diabetes" in result["extracted_data"]["diagnosis"]


def test_medication_extraction(clinical_notes):
    result = run_pipeline(clinical_notes[0])

    medications = result["extracted_data"]["medication"]
    assert any("Metformin" in item for item in medications)


def test_follow_up_extraction(clinical_notes):
    result = run_pipeline(clinical_notes[0])

    follow_up = result["extracted_data"]["follow_up"]
    assert len(follow_up) > 0


def test_summary_is_generated(clinical_notes):
    result = run_pipeline(clinical_notes[0])

    assert isinstance(result["summary"], str)
    assert len(result["summary"]) > 0


def test_all_30_notes_process_successfully(clinical_notes):
    results = [run_pipeline(note) for note in clinical_notes]

    assert len(results) == 30
    assert all("extracted_data" in item for item in results)
    assert all("summary" in item for item in results)


def test_json_output_contains_30_notes():
    output_file = os.path.join(
        PROJECT_ROOT,
        "outputs",
        "carebot_30_test_results.json"
    )

    assert os.path.exists(output_file)

    with open(output_file, "r", encoding="utf-8") as file:
        results = json.load(file)

    assert len(results) == 30


