

\# SLM Adaptation Decision



\## Selected Model

\- Model: Qwen2.5 1.5B

\- Runtime: Ollama

\- Quantization: Q4\_K\_M

\- License: Apache 2.0



\## Adaptation Method Implemented



This project uses prompt-based adaptation and FAQ-based retrieval.



1\. A healthcare-specific system prompt was created.

2\. A healthcare FAQ dataset was prepared.

3\. Keyword-based FAQ retrieval was implemented.

4\. The retrieved verified FAQ was passed to the local SLM.

5\. The model generated answers using the retrieved information.



\## LoRA / Fine-tuning Feasibility



Actual LoRA or QLoRA fine-tuning was not completed in this project.



The local environment has the following limitations:

\- NVIDIA RTX 2050 GPU with 4 GB VRAM.

\- PyTorch installed as a CPU-only build.

\- CUDA is not available in the current PyTorch environment.

\- Available system memory is limited.



\## Decision



Prompt-based adaptation and FAQ retrieval were selected as the practical adaptation approach for this prototype.



LoRA fine-tuning remains future work and requires a suitable training environment and further feasibility testing.



\## Important Limitation



Prompt-based adaptation and FAQ retrieval are not the same as model fine-tuning. The original Qwen2.5 model weights were not modified.



