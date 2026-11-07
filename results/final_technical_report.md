

\# Healthcare Customer Support SLM – Technical Report



\## 1. Project Overview



This project develops a local Small Language Model (SLM) application for healthcare customer support.



The application answers questions related to insurance claims and provider enrollment using a healthcare FAQ dataset and a locally running SLM.



\## 2. Project Objectives



\- Understand Small Language Models and their applications.

\- Select and run a task-specific SLM locally.

\- Prepare a healthcare FAQ dataset.

\- Evaluate baseline model responses.

\- Improve responses using prompt adaptation and FAQ retrieval.

\- Build and test a FastAPI application.

\- Measure response time and memory usage.



\## 3. Model Selection



Selected model: Qwen2.5 1.5B



| Property | Details |

|---|---|

| Parameters | 1.5 Billion |

| Architecture | Qwen2 |

| Context Length | 32,768 tokens |

| Quantization | Q4\_K\_M |

| Embedding Length | 1,536 |

| License | Apache 2.0 |

| Runtime | Ollama |



The model was downloaded and executed locally using Ollama. No hosted LLM API was used.



\## 4. Hardware and Environment



\- Operating System: Windows

\- Python: 3.13.15

\- Ollama: 0.40.11

\- RAM: 15.23 GB

\- CPU Cores: 12

\- GPU: NVIDIA RTX 2050 with 4 GB VRAM

\- PyTorch: 2.15.0+cpu

\- CUDA availability in PyTorch: False



\## 5. Dataset Preparation



A healthcare FAQ dataset was prepared with 20 question-and-answer records.



The dataset was divided into:



| Dataset | Records |

|---|---:|

| Training | 14 |

| Validation | 3 |

| Testing | 3 |

| Total | 20 |



Random seed: 42



The held-out test dataset was kept separate from adaptation.



\## 6. Baseline Evaluation



The original Qwen2.5 1.5B model was tested using healthcare customer support questions.



Initial testing identified limitations such as:

\- Missing important verification steps.

\- Generic answers to provider enrollment questions.

\- Difficulty answering denied-claim appeal questions.



Detailed results are available in baseline\_evaluation.md and baseline\_results.md.



\## 7. Adaptation Approach



Prompt-based adaptation and FAQ-based retrieval were implemented.



A healthcare-specific system prompt was created to:

\- Protect confidential information.

\- Require identity verification and authorization.

\- Avoid medical diagnosis and treatment advice.

\- Avoid inventing claim or policy information.



A keyword-based FAQ retrieval method was implemented. The retrieved FAQ answer was provided to the local SLM as context.



Note: This is prompt and retrieval adaptation, not model fine-tuning.



\## 8. Final Evaluation



Three held-out test questions were evaluated:



1\. Provider enrollment document requirements.

2\. Insurance claim status.

3\. Denied claim appeal process.



Observed result: 3 out of 3 test cases passed.



Observed pass rate: 100% (3/3).



This is a small prototype evaluation and does not establish production-level accuracy.



\## 9. Performance Benchmark



Test question: How can I check my insurance claim status?



| Metric | Result |

|---|---:|

| Response Time | 2.44 seconds |

| Python Process Memory Change | 0.32 MB |

| Test Status | Successful |



The memory measurement represents Python process memory change only, not total Ollama model memory consumption.



Only one benchmark run was recorded.



\## 10. API Deployment



A FastAPI application was created.



API endpoints:

\- GET `/` – checks API availability.

\- POST `/chat` – accepts a customer question and returns an SLM-generated answer.



The API was tested using Swagger UI at `/docs`.



Successful response: HTTP 200 OK.



Input validation and error handling were implemented.



\## 11. Fine-tuning Feasibility



LoRA/QLoRA fine-tuning was not completed.



The available environment uses CPU-only PyTorch and CUDA is unavailable. The GPU has 4 GB VRAM.



Prompt-based adaptation and FAQ retrieval were selected as the practical approach for this prototype.



Actual fine-tuning remains future work.



\## 12. Limitations



\- Small dataset containing 20 FAQ records.

\- Only 3 held-out test cases.

\- Keyword-based retrieval instead of embedding-based retrieval.

\- Single benchmark run.

\- LoRA fine-tuning not completed.

\- Further security, scalability and production testing required.



\## 13. Future Improvements



\- Expand the healthcare FAQ dataset.

\- Implement embedding-based semantic retrieval.

\- Explore LoRA fine-tuning in a suitable GPU environment.

\- Conduct larger evaluation with more test cases.

\- Measure full system resource consumption.

\- Improve API security and production deployment.



\## 14. Conclusion



This project demonstrates a locally running healthcare customer support application using Qwen2.5 1.5B, Ollama, FAQ retrieval and FastAPI.



The prototype successfully generated relevant answers for three held-out healthcare FAQ test cases and returned successful API responses.



The project demonstrates how a small language model can be adapted for a focused customer support task without using a hosted LLM API.



