# Evals (Evaluations) in AI Systems

The concept of **Evals** (Evaluations) is extremely important when building production-ready AI applications and AI agents.

Think of Evals as **automated testing for AI-generated outputs**, similar to integration testing in traditional software engineering.

<img src="./AI Evaluation Workflow Infographic.png" width="100%" />

---

## 1. What are Evals?

**Evals** (short for Evaluations) are systematic tests that measure whether an AI model or an entire AI system behaves according to predefined requirements.

They evaluate different dimensions:

- **Capability:** Can the AI perform the required task?
- **Quality:** Is the generated response accurate and useful?
- **Safety:** Does it avoid harmful or prohibited responses?
- **Reliability:** Does it produce consistent results?
- **Product Requirements:** Does it follow the business rules?

### Practical Example

Imagine you are building an AI-powered banking customer support chatbot. You want to verify that it:

- Answers banking questions correctly.
- Doesn't invent account information (hallucination).
- Doesn't expose sensitive customer data (PII).
- Follows banking policies and compliance rules.
- Escalates complaints to human support when necessary.

**Evals help automate these checks.**

---

## 2. How Do Evals Work?

Consider an AI application that generates responses to customer support emails.

```mermaid
flowchart TD
    D["1. Test Dataset<br/>(Questions & Expected Outcomes)"] --> A["2. AI Application Under Test<br/>(FastAPI + LLM + RAG)"]
    A -->|"Generated Response"| J["3. Evaluator / Judge<br/>(LLM-as-a-Judge / Python Rules)"]
    D -->|"Expected Criteria"| J
    J --> R["4. Evaluation Results<br/>(Scores, Pass/Fail, Metrics)"]
    R --> Dev["5. Developer Action<br/>(Analyze Failures & Optimize)"]
```

### AI Evaluation Workflow Steps

1. **Test Dataset:** Predefined dummy customer emails and expected outcomes.
   - *Example:* `"I was charged twice for my transaction."`
2. **AI Application:** Your application processes the customer request using an LLM and generates a customer support response.
3. **Evaluator (Judge):** Another AI model (LLM-as-a-Judge) or rule-based evaluator evaluates the generated response against evaluation criteria.
4. **Evaluation Results:**
   - Accuracy: `9/10`
   - Policy Compliance: `Pass`
   - Relevance: `8/10`
   - Hallucination: `Fail`
5. **Developer Action:** Analyze failures, improve prompts, retrieval, tools or models, and run the evals again.

> **Important Distinction:** The evaluator doesn't necessarily have to be another LLM. You can also use predefined rules, exact-match comparisons, custom Python functions, or human reviewers.

---

## 3. Evals vs Traditional Software Testing

| Traditional Testing | AI Evals |
|---|---|
| Tests application logic | Tests AI behaviour |
| Often expects exact results | Often evaluates semantic quality |
| Assertions and expected values | Scores, rubrics, and thresholds |
| Unit / integration tests | Model / system evaluations |
| Usually deterministic | Often probabilistic |

### Code Comparison

#### Traditional Test
```python
assert 2 + 3 == 5
```

#### AI Eval
```python
question = "What is the minimum balance?"
response = ai_application.generate(question)

score = evaluator.evaluate(
    question=question,
    response=response,
    expected_answer="As per account policy, the minimum balance is $500."
)

assert score["accuracy"] >= 0.8
```

---

## 4. Different Dimensions You Can Evaluate

For an enterprise AI chatbot or RAG system, you evaluate multiple dimensions:

| Evaluation Dimension | What It Checks |
|---|---|
| **Accuracy** | Is the answer factually correct? |
| **Relevance** | Does it answer the actual question asked? |
| **Faithfulness** | Is the answer strictly supported by the retrieved context? |
| **Hallucination** | Does it invent unverified information? |
| **Safety** | Does it generate harmful, biased, or prohibited content? |
| **Context Precision** | Are the retrieved documents relevant to the prompt? |
| **Context Recall** | Did the retrieval step find all necessary information? |
| **Latency** | How long does the end-to-end response take? |
| **Cost** | How much does each request cost in tokens? |
| **Tool Correctness** | Did the agent select and use the right tools with valid parameters? |

---

## 5. Why Are Evals Expensive?

Suppose you have **1,000 test cases**.

For each test case:
1. Your AI application invokes an LLM to generate an answer.
2. An evaluator invokes another LLM to judge that answer.
3. You pay for the tokens consumed by both operations.

```text
1,000 Test Cases  ===>  2,000 LLM Calls (1 Generation + 1 Judge per case)
```

### How to Reduce Evaluation Costs

- **Use deterministic Python assertions** wherever possible (regex, substring, schema validation).
- **Use smaller/faster models** (e.g., Llama 3 8B, Gemma 2B) as evaluators for simpler tasks.
- **Run evaluations on changed components only** (e.g., retrieval evals when changing embedding models).
- **Use representative sample test datasets** during development and full datasets before release.
- **Run expensive evaluations periodically** (nightly / CI/CD) rather than on every single iteration.

---

## 6. How Evals Fit into the AI Development Lifecycle

```mermaid
flowchart LR
    A["1. Create Dataset<br/>(Questions & Ground Truth)"] --> B["2. Query RAG App<br/>(FastAPI + Ollama)"]
    B --> C["3. Capture Outputs<br/>(Answer + Context)"]
    C --> D["4. Evaluate Metrics<br/>(Faithfulness, Correctness)"]
    D --> E["5. Store Results<br/>(Evaluation DB)"]
    E --> F["6. Display Dashboard"]
    F --> G["7. Improve Prompts / Models"]
    G --> A
```

### Practical Workflow

1. Create a dataset of questions and expected answers.
2. Send questions to your RAG application (FastAPI + Ollama + Qdrant).
3. Capture generated answers and retrieved documents.
4. Evaluate faithfulness, relevance, and correctness.
5. Record scores in an evaluation database.
6. Display results on a dashboard.
7. Improve prompts, retrieval configuration, or models.
8. Run the same evaluations again to check whether quality improved.

---

## 7. Evals vs Guardrails vs Observability

These three concepts work together to secure and optimize AI systems:

| Concept | Purpose | When It Runs | Example |
|---|---|---|---|
| **Evals** | Measure AI quality | Offline / CI/CD / Periodic | "Is the response accurate and faithful?" |
| **Guardrails** | Enforce restrictions in real-time | Online / Runtime (Inference) | Block sensitive PII or toxic prompt injection |
| **Observability** | Monitor actual production behaviour | Online / Post-execution | Track latency, error rate, token spend |

- **Evals** tell you whether your AI system is performing well.
- **Guardrails** help prevent unacceptable behaviour in real time.
- **Observability** helps you understand what is happening in production.

---

## 8. Practical Banking Chatbot Example

**Customer Request:**
> *"I forgot my internet banking password. Can you tell me how to reset it?"*

### Expected Evaluation Criteria

| Test Condition | Expected Result | Evaluation Method |
|---|---|---|
| Correct reset instructions provided | **Pass** | LLM Judge / Semantic Match |
| Requests customer password or OTP | **Fail** | Deterministic Python Check |
| Invents a fake reset URL | **Fail** | URL Allow-list Verification |
| Follows bank security policy | **Pass** | LLM Judge Rubric |
| Provides concise, relevant answer | **Pass** | Relevance Metric |

> **Production Consideration:** An LLM judge can itself make mistakes. For high-risk banking operations, do not rely exclusively on an LLM's score. Use deterministic security checks, authoritative policy validation, and human review where appropriate.

---

## 9. Setting Up Evals Between AI Systems: Step-by-Step

Let's understand how to set up an evaluation pipeline from absolute scratch.

### The Mental Model

```mermaid
flowchart TD
    subgraph Exam["The Exam Analogy"]
        T["Question Paper<br/>(Test Dataset)"]
        S["Student taking Exam<br/>(AI System Under Test)"]
        J["Teacher grading Exam<br/>(Evaluation System)"]
        M["Marks / Report Card<br/>(Evaluation Results)"]
    end
```

- **AI System A (Student):** Generates customer responses.
- **Evaluation System (Teacher):** Checks the responses.
- **Test Dataset (Question Paper):** Questions + Expected answers.
- **Evaluation Result (Marks):** Scores, Pass/Fail metrics.

---

### End-to-End System Architecture

```mermaid
flowchart TD
    subgraph Data["1. Test Data"]
        JSON["test_dataset.json<br/>Predefined questions & expected answers"]
    end

    subgraph App["2. System Under Test"]
        FastAPI["FastAPI AI Application<br/>(LLM + Qdrant RAG)"]
    end

    subgraph Engine["3. Evaluation Engine"]
        Runner["run_evals.py<br/>Orchestrator"]
        Judge["evaluator.py<br/>(Rule Checks + LLM Judge)"]
        Metrics["metrics.py<br/>(Accuracy, Safety, Relevance)"]
    end

    subgraph Output["4. Evaluation Output"]
        Report["results/report.json & Dashboard<br/>Accuracy: 90% | Safety: 100%"]
    end

    JSON --> Runner
    Runner -->|"Send Question"| FastAPI
    FastAPI -->|"Return Answer"| Runner
    Runner -->|"Question + Answer + Expected"| Judge
    Judge --> Metrics
    Metrics --> Runner
    Runner --> Report
```

---

### Step-by-Step Implementation

#### Step 1: Create Test Dataset (`test_dataset.json`)

```json
[
  {
    "id": "tc_001",
    "question": "How do I reset my banking password?",
    "expected": "Use the official password reset process on our website or app.",
    "banned_keywords": ["give me your password", "share password"]
  },
  {
    "id": "tc_002",
    "question": "Can I share my OTP with customer care?",
    "expected": "Never share your OTP with anyone, including bank staff.",
    "banned_keywords": ["yes", "share it"]
  },
  {
    "id": "tc_003",
    "question": "What is a fixed deposit?",
    "expected": "A fixed deposit is a financial instrument where money is deposited for a fixed tenure at an agreed interest rate.",
    "banned_keywords": []
  }
]
```

#### Step 2: Query Your AI Application Under Test

```python
# test_client.py
import requests

def get_ai_response(question: str) -> str:
    response = requests.post(
        "http://localhost:8000/api/chat",
        json={"question": question}
    )
    return response.json()["answer"]
```

#### Step 3: Evaluate the Response

You can combine **deterministic rule checks** and **LLM-as-a-Judge**:

```python
# evaluator.py
from typing import Dict, Any

def evaluate_safety_rules(response: str, banned_keywords: list) -> bool:
    for word in banned_keywords:
        if word.lower() in response.lower():
            return False
    return True

def llm_judge(question: str, generated_answer: str, expected_answer: str) -> Dict[str, Any]:
    judge_prompt = f"""
    You are an expert AI evaluator.
    Evaluate the following response based on correctness and relevance.

    Question: {question}
    Generated Answer: {generated_answer}
    Expected Answer: {expected_answer}

    Return JSON:
    {{
        "correctness_score": <0.0 to 1.0>,
        "is_safe": <true/false>,
        "reasoning": "<short explanation>"
    }}
    """
    # Call judge LLM (e.g. via Ollama or API)
    # result = call_judge_llm(judge_prompt)
    return {"correctness_score": 0.95, "is_safe": True, "reasoning": "Accurate and safe."}
```

#### Step 4: Run and Generate Results

```python
# run_evals.py
import json

def run_evaluation_suite():
    with open("test_dataset.json") as f:
        dataset = json.load(f)

    results = []
    for item in dataset:
        generated = get_ai_response(item["question"])
        safety_pass = evaluate_safety_rules(generated, item["banned_keywords"])
        judge_res = llm_judge(item["question"], generated, item["expected"])

        results.append({
            "id": item["id"],
            "question": item["question"],
            "generated": generated,
            "safety": safety_pass and judge_res["is_safe"],
            "accuracy": judge_res["correctness_score"]
        })

    # Summary
    avg_accuracy = sum(r["accuracy"] for r in results) / len(results)
    safety_rate = sum(1 for r in results if r["safety"]) / len(results) * 100

    print(f"Evaluation Complete!")
    print(f"Accuracy: {avg_accuracy * 100:.1f}%")
    print(f"Safety Compliance: {safety_rate:.1f}%")

if __name__ == "__main__":
    run_evaluation_suite()
```

---

## 10. Suggested Local Project Structure

```text
enterprise-rag-project/
├── app/
│   ├── main.py          # FastAPI AI application
│   ├── rag.py           # Retrieval and LLM logic
│   └── database.py      # Qdrant client connection
├── evals/
│   ├── test_dataset.json # Test cases & ground truth
│   ├── run_evals.py     # Evaluation runner / CLI
│   ├── evaluator.py     # Deterministic & LLM judges
│   └── metrics.py       # Scoring functions & rubrics
├── results/
│   └── latest_run.json  # Stored evaluation reports
└── tests/
    └── test_evals.py    # Pytest integration for CI/CD
```

---

## 11. CI/CD Integration with GitHub Actions

Automate your evaluations on every prompt change or model update:

```mermaid
flowchart TD
    Dev["Developer modifies prompt / model"] --> Commit["Git Commit & Push"]
    Commit --> CI["GitHub Actions Triggered"]
    CI --> Run["Run Automated Evals Suite"]
    Run --> Check{"Accuracy >= 90% and Safety == 100%?"}
    Check -->|"Yes (PASS)"| Deploy["Continue Deployment"]
    Check -->|"No (FAIL)"| Block["Block PR & Notify Developer"]
```

---

## 12. Quick Comprehension Check

> **Question:** You build an AI banking chatbot. It generates an incorrect answer to a customer. Which component is responsible for identifying this problem during automated evaluation?
> 
> - A. Customer
> - B. Evaluation Engine
> - C. Qdrant database
> - D. FastAPI server alone

**Correct Answer:** **B. Evaluation Engine**

*Explanation:* The Evaluation Engine checks the AI-generated answer against expected answers, evaluation criteria, and safety rules. It reports failures so developers can fix them before reaching production.

---

## Key Takeaway

> **Evals = Automated Quality Assurance for AI Systems**
>
> - **Traditional software testing** checks whether code executes as expected deterministically.
> - **AI Evals** check whether probabilistic AI outputs meet defined quality, safety, faithfulness, and business requirements.
>
> **Your AI application generates the answer. Your Evaluation Engine checks whether that answer is good enough.**
