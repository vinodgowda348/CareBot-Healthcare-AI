import sys
import os
import json

# Allow Python to find the files inside src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pipeline import run_pipeline


# 30 synthetic clinical notes
# No real patient information is used.
clinical_notes = [
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


results = []

for i, note in enumerate(clinical_notes, start=1):
    result = run_pipeline(note)

    results.append({
        "test_note_id": i,
        "clinical_note": note,
        "extracted_data": result["extracted_data"],
        "summary": result["summary"]
    })


# Save structured JSON output
output_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "carebot_30_test_results.json")

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=2, ensure_ascii=False)


print("=== CAREBOT 30-NOTE TEST ===")
print("Total notes processed:", len(results))
print("JSON output:", output_file)

for result in results:
    print(f"\n--- Note {result['test_note_id']} ---")
    print("Extracted:", result["extracted_data"])
    print("Summary:", result["summary"])

print("\n30-note test completed successfully.")