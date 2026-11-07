

\# Healthcare Customer Support SLM



A local AI-powered healthcare customer support application built using Qwen2.5 1.5B, Ollama, FAQ-based retrieval and FastAPI.



\## Project Overview



This project demonstrates how a Small Language Model (SLM) can support healthcare customer service questions related to insurance claims and provider enrollment.



The application uses a locally running model and a healthcare FAQ dataset. It does not use a hosted LLM API.



\## Technology Stack



\- Python 3.13

\- Qwen2.5 1.5B

\- Ollama

\- FastAPI

\- Pydantic

\- JSON dataset

\- Keyword-based FAQ retrieval



\## Model Details



| Property | Value |

|---|---|

| Model | Qwen2.5 1.5B |

| Parameters | 1.5 Billion |

| Quantization | Q4\_K\_M |

| Context Length | 32,768 |

| License | Apache 2.0 |

| Runtime | Ollama |



\## Project Structure



```text

healthcare-customer-support-slm/

│

├── data/

│   ├── healthcare\_faq.json

│   ├── healthcare\_faq\_day2.json

│   ├── train.json

│   ├── validation.json

│   └── test.json

│

├── results/

│   ├── baseline\_results.md

│   ├── baseline\_evaluation.md

│   ├── prompt\_adaptation\_evaluation.md

│   ├── rag\_evaluation.md

│   ├── final\_evaluation.md

│   ├── benchmark\_results.md

│   ├── hardware\_check.md

│   ├── adaptation\_decision.md

│   └── final\_technical\_report.md

│

├── benchmark.py

├── faq\_retrieval.py

├── healthcare\_prompt.txt

├── healthcare\_rag.py

├── main.py

├── split\_dataset.py

└── .gitignore

```



\## Setup Instructions



\### 1. Install Python



Install Python 3.13 or a compatible version.



\### 2. Install Ollama



Download and install Ollama:



https://ollama.com/



\### 3. Download the model



Run:



```bash

ollama pull qwen2.5:1.5b

```



\### 4. Create virtual environment



```bash

python -m venv .venv

```



Activate on Windows PowerShell:



```powershell

.venv\\Scripts\\Activate.ps1

```



\### 5. Install dependencies



```bash

pip install fastapi uvicorn pydantic psutil numpy

```



\### 6. Start the API



From the project directory, run:



```bash

python -m uvicorn main:app --reload

```



\## API Usage



Open Swagger UI:



http://127.0.0.1:8000/docs



Endpoint:



`POST /chat`



Example request:



```json

{

&#x20; "question": "How can I check my insurance claim status?"

}

```



The API returns a healthcare customer support answer generated using the local SLM.



\## Evaluation Results



\- Held-out test cases: 3

\- Passed test cases: 3

\- Observed pass rate: 100% (3/3)

\- Recorded response time: 2.44 seconds

\- Python process memory change: 0.32 MB



Note: This is a small prototype evaluation. The memory measurement does not represent total Ollama model memory usage.



\## Adaptation Approach



The project implements:



\- Healthcare-specific prompt adaptation.

\- Keyword-based FAQ retrieval.

\- Retrieval-augmented answer generation using the local SLM.



Actual LoRA/QLoRA fine-tuning was not completed due to the available hardware and PyTorch environment limitations.



\## Limitations



\- Small healthcare FAQ dataset.

\- Only three held-out test cases.

\- Keyword-based retrieval rather than embedding-based semantic retrieval.

\- Single benchmark run.

\- No actual model fine-tuning.

\- Additional security and production testing required.



\## Future Improvements



\- Expand the healthcare FAQ dataset.

\- Implement embedding-based semantic retrieval.

\- Explore LoRA fine-tuning using suitable GPU hardware.

\- Increase evaluation test cases.

\- Improve API security and deployment.



\## Author



Lavanya



\## License



Qwen2.5 model is distributed under Apache License 2.0. Refer to the model's official license and terms for details.



