
import json
import re
import subprocess

# Load healthcare instructions
with open("healthcare_prompt.txt", encoding="utf-8") as file:
    system_prompt = file.read()

# Load FAQ dataset
with open("data/healthcare_faq_day2.json", encoding="utf-8") as file:
    faqs = json.load(file)


# Search matching FAQ
def search_faq(user_question):
    question_words = set(re.findall(r"\w+", user_question.lower()))

    results = []

    for faq in faqs:
        faq_words = set(re.findall(r"\w+", faq["question"].lower()))
        score = len(question_words & faq_words)
        results.append((score, faq))

    results.sort(key=lambda item: item[0], reverse=True)

    if results and results[0][0] > 0:
        return results[0][1]

    return None


# Generate answer using local SLM
def generate_answer(question):
    faq = search_faq(question)

    if faq is None:
        return None

    prompt = f"""
{system_prompt}

Verified FAQ:
Question: {faq['question']}
Answer: {faq['answer']}

Customer question: {question}

Answer using only the verified FAQ information.
Do not invent information.
"""

    result = subprocess.run(
        ["ollama", "run", "qwen2.5:1.5b", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120
    )

    if result.returncode == 0:
        return result.stdout.strip()

    raise RuntimeError(result.stderr)
