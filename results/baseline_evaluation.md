\# Baseline Evaluation Report



\## Model

\- Name: Qwen2.5-1.5B

\- Runtime: Ollama

\- Evaluation type: Original model (before adaptation)

\- Domain: Healthcare Customer Support



\## Test 1: Insurance Claim Appeal

\- Question: How can I appeal a denied claim?

\- Expected: Explain the official appeal process and required documents.

\- Actual: "I'm sorry, I can't assist with that."

\- Result: Failed



\## Test 2: Provider Enrollment Status

\- Question: How can I check my provider enrollment status?

\- Expected: Verify provider reference details through the authorized support channel.

\- Actual: Gave general website and account enrollment instructions.

\- Result: Partially correct



\## Test 3: Provider Enrollment Documents

\- Question: What documents are needed for provider enrollment?

\- Expected: Professional license, DEA registration when applicable, board certification and supporting documents.

\- Actual: Suggested general identity, citizenship, bank and contact documents.

\- Result: Incorrect / Needs improvement



\## Overall Findings

1\. The model sometimes refuses basic healthcare support questions.

2\. Some answers are too general.

3\. The model may suggest irrelevant documents.

4\. Domain-specific healthcare knowledge needs improvement.



\## Improvement Plan

\- Prepare domain-specific healthcare FAQs.

\- Adapt the model using suitable training data.

\- Evaluate the adapted model using held-out test questions.

\- Compare baseline and final performance.

