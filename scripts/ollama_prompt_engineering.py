import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

SYSTEM_PROMPT = """
You are CareBot, a healthcare AI assistant.
Answer clearly and professionally.
Summarize clinical information without inventing facts.
If information is missing, say that it is not provided.
Do not give a medical diagnosis or replace a healthcare professional.
"""


def ask_ollama(user_prompt):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["message"]["content"]


if __name__ == "__main__":
    prompts = [
        "What is a clinical note?",
        "Summarize: Patient has fever and cough for three days.",
        "Extract the diagnosis from: The patient was diagnosed with influenza.",
        "Why is follow-up information important in a clinical note?",
        "Explain the difference between symptoms and diagnosis."
    ]

    for i, prompt in enumerate(prompts, start=1):
        print("\n" + "=" * 60)
        print(f"PROMPT {i}: {prompt}")
        print("=" * 60)
        print(ask_ollama(prompt))