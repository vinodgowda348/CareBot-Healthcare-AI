import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

QUESTIONS = [
    "What is a clinical note?",
    "What is the difference between symptoms and diagnosis?",
    "Why is follow-up information important in healthcare?"
]

MODELS = [
    "llama3.2:3b",
    "qwen2.5:3b"
]


def ask_model(model, question):
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Answer clearly, accurately, and concisely. Do not invent information."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["message"]["content"]


for question_number, question in enumerate(QUESTIONS, start=1):
    print("\n" + "=" * 70)
    print(f"QUESTION {question_number}: {question}")
    print("=" * 70)

    for model in MODELS:
        print(f"\n--- {model} ---")
        print(ask_model(model, question))