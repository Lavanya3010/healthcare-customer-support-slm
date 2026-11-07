\# FAQ-Based RAG Evaluation



Model: Qwen2.5-1.5B

Runtime: Ollama

Method: Keyword-based FAQ retrieval + healthcare instruction prompt



\## Test Question

How can I check my insurance claim status?



\## Retrieved FAQ

Verify the customer's identity and authorization first.

Then use the approved system to check the claim reference number

and provide the available status.



\## Model Result

The model included identity verification, authorization

and approved-system usage in its response.



\## Observation

FAQ context improved the relevance of the response.

However, the model added a claim reference number promise

that was not explicitly supported by the FAQ.



\## Limitation

This experiment uses keyword-based retrieval, not vector search.

