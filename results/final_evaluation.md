\# Final SLM Evaluation



Model: Qwen2.5-1.5B

Runtime: Ollama

Adaptation: Healthcare prompt + keyword-based FAQ retrieval



\## Test Results



| Test Case | Result |

|---|---|

| Provider enrollment documents | Pass |

| Insurance claim status | Pass |

| Denied claim appeal | Pass |



Total test cases: 3

Passed: 3

Failed: 0



Observed test pass rate: 100% (3/3)



\## Findings



The application retrieved relevant FAQ records and generated

responses containing the expected information for all three

held-out test questions.



\## Limitations



\- Only three held-out test cases were evaluated.

\- Retrieval uses keyword matching, not vector embeddings.

\- Prompt and FAQ-based adaptation were used.

\- LoRA fine-tuning has not been completed.

\- Larger evaluation datasets are needed for reliable results.

