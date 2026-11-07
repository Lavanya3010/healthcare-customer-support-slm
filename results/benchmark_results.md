

\# SLM Performance Benchmark Results



\## Model Details

\- Model: Qwen2.5 1.5B

\- Quantization: Q4\_K\_M

\- Runtime: Ollama

\- Execution: Local system



\## Test Question

How can I check my insurance claim status?



\## Model Response

Verify the customer's identity and authorization. Then use the approved system to check the claim reference number and provide the available status.



\## Benchmark Measurements



| Metric | Result |

|---|---:|

| Response Time | 2.44 seconds |

| Python Process Memory Change | 0.32 MB |

| Test Status | Successful |



\## Observation

The local SLM generated a relevant healthcare customer support response in 2.44 seconds.



Note: Memory change represents the Python process only. It does not represent the total memory used by the Ollama model.



\## Limitation

This is a single-question benchmark. More test runs are required for reliable average latency and memory measurements.



