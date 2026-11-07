import json
import re

with open("data/healthcare_faq_day2.json", encoding="utf-8") as file:
    faqs = json.load(file)


def search_faq(user_question):
    question_words = set(re.findall(r"\w+", user_question.lower()))

    scored_faqs = []

    for faq in faqs:
        faq_words = set(re.findall(r"\w+", faq["question"].lower()))
        score = len(question_words & faq_words)

        scored_faqs.append((score, faq))

    scored_faqs.sort(key=lambda item: item[0], reverse=True)

    return scored_faqs[0][1] if scored_faqs and scored_faqs[0][0] > 0 else None


query = "How can I check my insurance claim status?"
result = search_faq(query)

if result:
    print("Matched FAQ:", result["question"])
    print("FAQ Answer:", result["answer"])
else:
    print("No matching FAQ found.")