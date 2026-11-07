
import time
import psutil
import os

from healthcare_rag import generate_answer

process = psutil.Process(os.getpid())

question = "How can I check my insurance claim status?"

memory_before = process.memory_info().rss / (1024 * 1024)

start_time = time.time()

answer = generate_answer(question)

end_time = time.time()

memory_after = process.memory_info().rss / (1024 * 1024)

response_time = end_time - start_time
memory_used = memory_after - memory_before

print("\n--- SLM PERFORMANCE BENCHMARK ---")
print("Question:", question)
print("Answer:", answer)
print(f"Response Time: {response_time:.2f} seconds")
print(f"Python Process Memory Change: {memory_used:.2f} MB")
