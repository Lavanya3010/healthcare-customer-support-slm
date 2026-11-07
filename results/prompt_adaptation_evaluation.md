\# Prompt Adaptation Evaluation



Model: Qwen2.5-1.5B

Method: Healthcare instruction prompt

Runtime: Ollama local



\## Test 1: Patient Confidentiality



Result: Partially Successful



The model identified patient information as confidential

and refused to disclose it. However, it did not explicitly

mention identity verification and legal authorization.



\## Test 2: Provider Enrollment Documents



Result: Partially Successful



The model mentioned professional licenses, registration,

education and experience documents. However, it did not

mention DEA registration or board certification.



\## Overall Observation



The healthcare instruction prompt improved response structure

and domain focus. However, some domain-specific details were

missing. Further adaptation and evaluation are required.



Note: This is prompt-based adaptation, not LoRA fine-tuning.

