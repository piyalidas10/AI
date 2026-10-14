# AI Evals

AI evals (evaluations) are systematic quality checks and test suites that measure the accuracy, reliability, and behavior of Large Language Models (LLMs), RAG pipelines, and autonomous AI agents. Unlike traditional software unit tests that check for exact deterministic outputs, AI evals handle **non-deterministic and stochastic outputs**.

---

## Core Components of an Eval

Every evaluation consists of three main elements:

| Component | Description |
|-----------|-------------|
| **Data (Inputs)** | A set of representative prompts, queries, or user scenarios (including edge cases). |
| **Task** | The AI model, chain, or agent processing the input to produce an output. |
| **Score (Grader)** | Grading logic or a metric scoring function that rates the output on a normalized scale (such as 0 to 1, or pass/fail). |

---

## Common Types of AI Evals

- **Code Assertions**: Programmatic checks for objective rules like JSON structure, character/word limits, substring searches, or syntax validation.
- **Golden Datasets**: Static test sets with specific inputs and known "right answers" or expected reference outputs.
- **LLM-as-a-Judge**: Using a secondary, often more capable LLM to evaluate semantic quality, tone, relevance, faithfulness, or brand fit against a rubric.
- **Human Feedback / Review**: Manual inspection, annotations, and ratings by domain experts or users to capture nuanced subjective quality.

---

## Types of Product Evals

- **Capability Evals**: Test what an AI agent or model can do well, targeting tasks with lower initial pass rates to drive improvements.
- **Regression Evals**: Run continuously with a near 100% pass rate to ensure new code, prompt changes, or model updates do not break existing functionality.

---

## How to Implement Evals (The Workflow)

1. **Error Analysis**: Review production logs and interaction traces (inputs, tool calls, outputs) to identify real failure modes.
2. **Metric Selection**: Choose code checks, golden sets, or LLM judges that match the specific nature of the error.
3. **Continuous Iteration**: Run evals pre-launch, after every prompt/model tweak, and continuously in production to monitor quality, latency, and cost.

---

## Why Product Teams Need Evals

Evals help answer: *"How do I know if this is consistently good across all customers and target use cases?"*

- With **traditional software**, outputs are deterministic — unit tests verify exact outcomes every time.
- With **LLMs**, outputs are probabilistic — the same input can yield different outputs. Evals measure the *rate* at which the model returns a correct response.
- Correctness is often **context-dependent** (e.g., a student vs. a professor need different levels of detail). Don't let a vendor define correctness for your product — that is the product team's job.

---

## The Structure of an Evaluation

An evaluation ("eval") is a test for an AI system: give an AI an input, then apply grading logic to its output to measure success. This covers automated evals that can be run during development without real users.

### Evaluation Complexity Levels

| Level | Description |
|-------|-------------|
| **Single-turn** | A prompt, a response, and grading logic. Straightforward: was the output correct? The dominant method for earlier LLMs. |
| **Multi-turn** | The agent receives tools, a task, and an environment; executes an agent loop (tool calls + reasoning); updates the environment. Grading verifies the final state (e.g., unit tests on a working implementation). |
| **Agent (full)** | Agents use tools across many turns, modifying state and adapting as they go. Mistakes can propagate and compound. Frontier models may also find creative solutions that surpass the limits of static evals — e.g., Opus 4.5 solved a τ2-Bench flight-booking problem by discovering a loophole in the policy. It "failed" the eval as written, but produced a better outcome for the user. |

### Key Terms

| Term | Definition |
|------|------------|
| **Task** | A single test with defined inputs and success criteria (also called a problem or test case). |
| **Trial** | A single attempt at a task. Multiple trials are run to account for non-determinism and produce more consistent results. |
| **Grader** | Logic that scores some aspect of the agent's performance. A task can have multiple graders, each containing multiple assertions (checks). |
| **Transcript / Trace / Trajectory** | The complete record of a trial — outputs, tool calls, reasoning, intermediate results, and all interactions. For the Anthropic API, this is the full `messages` array at the end of the eval run. |
| **Outcome** | The final state in the environment at the end of the trial. A flight-booking agent may say "Your flight has been booked," but the outcome is whether a reservation actually exists in the environment's SQL database. |
| **Evaluation Harness** | The infrastructure that runs evals end-to-end. It provides instructions and tools, runs tasks concurrently, records all steps, grades outputs, and aggregates results. |
| **Agent Harness (Scaffold)** | The system that enables a model to act as an agent: processes inputs, orchestrates tool calls, and returns results. When evaluating "an agent," you are evaluating the harness and the model working together. |
| **Evaluation Suite** | A collection of tasks designed to measure specific capabilities or behaviors. Tasks in a suite share a broad goal (e.g., a customer support eval suite might test refunds, cancellations, and escalations). |

---

## Types of Graders for Agents

Agent evaluations typically combine three types of graders: code-based, model-based, and human. Each grader evaluates some portion of either the transcript or the outcome. An essential component of effective evaluation design is choosing the right grader for the job.

### Code-Based Graders

| | Detail |
|-|--------|
| **Methods** | String match checks (exact, regex, fuzzy), binary tests (fail-to-pass, pass-to-pass), static analysis (lint, type, security), outcome verification, tool call verification (tools used, parameters), transcript analysis (turns taken, token usage) |
| **Strengths** | Fast · Cheap · Objective · Reproducible · Easy to debug · Verify specific conditions |
| **Weaknesses** | Brittle to valid variations that don't match expected patterns exactly · Lacking in nuance · Limited for evaluating subjective tasks |

### Model-Based Graders (LLM-as-a-Judge)

| | Detail |
|-|--------|
| **Methods** | Rubric-based scoring, natural language assertions, pairwise comparison, reference-based evaluation, multi-judge consensus |
| **Strengths** | Flexible · Scalable · Captures nuance · Handles open-ended tasks · Handles freeform output |
| **Weaknesses** | Non-deterministic · More expensive than code · Requires calibration with human graders for accuracy |

> **Best practices for LLM-as-a-Judge:**
> 1. Give the judge a **much simpler task** than the original model received.
> 2. Define criteria so the judge returns a **binary response** (true/false, yes/no).
> 3. **Align the judge** with your own judgment through calibration against human experts.
> 4. **Account for judge error** when reporting eval error rates — judges always make some mistakes.
> 5. Give the judge a **way out** (e.g., return "Unknown") when it lacks sufficient information — avoids hallucinated judgments.
> 6. Grade each dimension with a **separate, isolated judge** rather than one judge for all dimensions.

### Human Graders

| | Detail |
|-|--------|
| **Methods** | SME review, crowdsourced judgment, spot-check sampling, A/B testing, inter-annotator agreement |
| **Strengths** | Gold-standard quality · Matches expert user judgment · Used to calibrate model-based graders |
| **Weaknesses** | Expensive · Slow · Often requires access to human experts at scale |

### Scoring Strategies

For each task, scoring can be:
- **Weighted** — combined grader scores must hit a threshold.
- **Binary** — all graders must pass.
- **Hybrid** — a mix of weighted and binary requirements.
- **Partial credit** — for multi-component tasks, a support agent that correctly identifies the problem but fails to process a refund is meaningfully better than one that fails immediately.

---

## Choosing the Right Eval Type

| Error Type | Eval Type | Reason |
|------------|-----------|--------|
| A quote wasn't actually said | Code assertion | A quote either appears verbatim in the transcript or it doesn't. No judgment required. |
| A claim wasn't grounded in the transcript | LLM-as-a-Judge | The model can invent a claim using entirely different words — no string to search for. |
| Agent suggested a general question | Code assertion | A short list of red-flag words reliably catches these. |
| Agent suggested a leading question | LLM-as-a-Judge | Requires judging whether a question presumes an answer — no fixed wording to look for. |
| Two differently worded items are the same | Golden Dataset | Small inputs, small output, one right answer. Easy to label and reuse. |
| A tree branch is missing a sub-grouping | Code assertion + LLM-as-a-Judge | Counting children is cheap; only flagged nodes get sent to the judge. |

> **Rule of thumb**: Start with the simplest, most deterministic measurement. Only escalate to an LLM judge when judgment is genuinely required.

---

## Handling Non-Determinism in Agent Evals

Because agent outputs vary between runs, two metrics are used to capture this:

- **pass@k** — The probability that at least one of *k* trials succeeds. Rises as *k* increases. Used when one success is sufficient (e.g., code generation tools).
- **pass^k** — The probability that *all k* trials succeed. Falls as *k* increases. Used when consistent reliability is required (e.g., customer-facing agents).

At `k=1` both metrics are equal. As `k` grows, they diverge sharply — `pass@k` approaches 100% while `pass^k` approaches 0%.

---

## Evaluating by Agent Type

Several common types of agents are deployed at scale today: coding, conversational, research, and computer use agents. Each type may be deployed across many industries, but they can be evaluated using similar techniques — use these as a foundation and extend them to your domain.

### Coding Agents

Coding agents write, test, and debug code, navigating codebases and running commands like a human developer.

- Use **deterministic graders** — does the code run and do the tests pass? Software is generally straightforward to evaluate.
- Supplement with heuristics-based **code quality rules** (LLM rubric) and **static analysis** (ruff, mypy, bandit).
- Grade the **transcript** as well: assess how the agent calls tools or interacts with the user.
- Reference benchmarks: **SWE-bench Verified** (GitHub issues graded by test suite pass/fail; LLMs progressed from 40% → >80% in one year), **Terminal-Bench** (end-to-end CLI tasks like building a Linux kernel from source).

**Example eval task — fixing an authentication bypass vulnerability:**

```yaml
task:
  id: "fix-auth-bypass_1"
  desc: "Fix authentication bypass when password field is empty and ..."
  graders:
    - type: deterministic_tests
      required: [test_empty_pw_rejected.py, test_null_pw_rejected.py]
    - type: llm_rubric
      rubric: prompts/code_quality.md
    - type: static_analysis
      commands: [ruff, mypy, bandit]
    - type: state_check
      expect:
        security_logs: {event_type: "auth_blocked"}
    - type: tool_calls
      required:
        - {tool: read_file, params: {path: "src/auth/*"}}
        - {tool: edit_file}
        - {tool: run_tests}
  tracked_metrics:
    - type: transcript
      metrics: [n_turns, n_toolcalls, n_total_tokens]
    - type: latency
      metrics: [time_to_first_token, output_tokens_per_sec, time_to_last_token]
```

> In practice, coding evaluations typically rely on unit tests for correctness and an LLM rubric for code quality. Additional graders and metrics are added only as needed.

---

### Conversational Agents

Conversational agents interact with users in support, sales, or coaching. Unlike traditional chatbots, they maintain state, use tools, and take actions mid-conversation. The quality of the interaction itself is part of what is being evaluated.

- Use **verifiable end-state outcomes** and rubrics that capture both task completion and interaction quality.
- Often require a **second LLM to simulate the user** (used in alignment auditing to stress-test models through adversarial conversations).
- Success is **multidimensional**: is the ticket resolved (state check)? Did it finish in <10 turns (transcript constraint)? Was the tone appropriate (LLM rubric)?
- Reference benchmarks: **τ-Bench**, **τ2-Bench** (simulate multi-turn interactions in retail support and airline booking).

**Example eval task — handling a refund for a frustrated customer:**

```yaml
graders:
  - type: llm_rubric
    rubric: prompts/support_quality.md
    assertions:
      - "Agent showed empathy for customer's frustration"
      - "Resolution was clearly explained"
      - "Agent's response grounded in fetch_policy tool results"
  - type: state_check
    expect:
      tickets: {status: resolved}
      refunds: {status: processed}
  - type: tool_calls
    required:
      - {tool: verify_identity}
      - {tool: process_refund, params: {amount: "<=100"}}
      - {tool: send_confirmation}
  - type: transcript
    max_turns: 10
tracked_metrics:
  - type: transcript
    metrics: [n_turns, n_toolcalls, n_total_tokens]
  - type: latency
    metrics: [time_to_first_token, output_tokens_per_sec, time_to_last_token]
```

> In practice, conversational agent evaluations typically use model-based graders to assess both communication quality and goal completion — many tasks (like answering a question) have multiple correct solutions.

---

### Research Agents

Research agents gather, synthesize, and analyze information, producing outputs like answers or reports. Unlike coding agents where unit tests provide binary signals, research quality can only be judged relative to the task.

**Unique challenges:**
- Experts may disagree on whether a synthesis is comprehensive.
- Ground truth shifts as reference content changes constantly.
- Longer, open-ended outputs create more room for mistakes.

**Grader strategy — combine types:**

| Grader | What It Checks |
|--------|---------------|
| **Groundedness check** | Are claims supported by retrieved sources? |
| **Coverage check** | Are all key facts a good answer must include present? |
| **Source quality check** | Are the sources authoritative, not just the first retrieved? |
| **Exact match** | For factual questions with objectively correct answers (e.g., "What was Company X's Q3 revenue?"). |
| **LLM rubric** | Flags unsupported claims, gaps in coverage, and verifies coherence of open-ended synthesis. |

- Reference benchmark: **BrowseComp** (finding hard-to-locate facts across the open web — easy to verify, hard to solve).
- LLM-based rubrics must be **frequently calibrated against expert human judgment** given the subjective nature of research quality.

---

### Computer Use Agents

Computer use agents interact with software via screenshots, mouse clicks, keyboard inputs, and scrolling — through the same interface as humans, rather than APIs.

- Evaluation requires running the agent in a **real or sandboxed environment**.
- Grade by inspecting the **environment state after task completion**: file system, application configs, database contents, UI element properties.
- **DOM-based interactions** are fast but token-heavy; **screenshot-based interactions** are slower but more token-efficient. Evals should verify the agent selects the right modality for each context.
- Reference benchmarks: **WebArena** (browser-based tasks with URL and page state checks + backend state verification), **OSWorld** (full OS-level control with post-task environment inspection).

---

## Roadmap: Going from Zero to Reliable Evals

Think of this as a roadmap for eval-driven agent development: define success early, measure it clearly, and iterate continuously.

### Phase A — Collect Tasks for the Initial Eval Dataset

**Step 0 — Start early**

Teams delay building evals thinking they need hundreds of tasks. In reality, **20–50 simple tasks drawn from real failures is a great start**. In early agent development, each system change has a large, noticeable impact — small sample sizes suffice. More mature agents may need larger, harder evals to detect smaller effects, but take the 80/20 approach in the beginning.

> Evals get harder to build the longer you wait. Early on, product requirements naturally translate into test cases. Wait too long and you're reverse-engineering success criteria from a live system.

---

**Step 1 — Start with what you already test manually**

Begin with the manual checks you run during development — the behaviors you verify before each release and common tasks end users try. If already in production, look at your bug tracker and support queue. Converting user-reported failures into test cases ensures your suite reflects actual usage; prioritizing by user impact focuses effort where it counts.

---

**Step 2 — Write unambiguous tasks with reference solutions**

A good task is one where **two domain experts would independently reach the same pass/fail verdict**. Ambiguity in task specifications becomes noise in metrics. The same applies to model-based grader criteria — vague rubrics produce inconsistent judgments.

- Each task should be passable by an agent that follows instructions correctly.
- A **0% pass rate across many trials** (0% pass@100) is most often a signal of a broken task specification, not an incapable agent.
- Create a **reference solution** for each task: a known working output that passes all graders. This proves the task is solvable and verifies graders are correctly configured.

> **Example pitfall**: Terminal-Bench audits revealed that if a task asks the agent to write a script without specifying a filepath, and tests assume a particular filepath, the agent fails through no fault of its own.

---

**Step 3 — Build balanced problem sets**

Test both cases where a behavior **should** occur and where it **should not**. One-sided evals create one-sided optimization.

> **Example**: Building evals for web search in Claude.ai required covering both directions — queries where the model should search (e.g., "What's the weather?") and queries where it should answer from existing knowledge (e.g., "Who founded Apple?"). Striking the right balance between undertriggering and overtriggering took many rounds of refinements.

---

### Phase B — Design the Eval Harness and Graders

**Step 4 — Build a robust eval harness with a stable environment**

The agent in the eval must function roughly the same as the production agent. Each trial should be **isolated** by starting from a clean environment.

- Unnecessary shared state between runs (leftover files, cached data, resource exhaustion) causes correlated failures due to infrastructure flakiness — not agent performance.
- Shared state can also **artificially inflate** performance (e.g., Claude gaining an unfair advantage by examining git history from previous trials).
- If multiple distinct trials fail due to the same environmental constraint (e.g., limited CPU memory), those trials are not independent and the results become unreliable.

---

**Step 5 — Design graders thoughtfully**

- **Prefer deterministic graders** where possible; use LLM graders where necessary; use human graders judiciously for validation.
- **Grade what the agent produced, not the path it took.** Checking for a specific sequence of tool calls is too rigid — agents regularly find valid approaches that eval designers didn't anticipate.
- **Build in partial credit** for multi-component tasks.
- **Calibrate LLM judges closely with human experts.** Give the LLM a way out (return "Unknown" when information is insufficient). Grade each dimension with an isolated judge rather than one judge for all dimensions.
- **Make graders resistant to bypasses.** Agents shouldn't be able to cheat the eval — passing should genuinely require solving the problem.

> **Real-world grading bug**: Opus 4.5 initially scored 42% on CORE-Bench. An Anthropic researcher discovered rigid grading that penalized "96.12" when expecting "96.124991…", ambiguous task specs, and stochastic tasks impossible to reproduce exactly. After fixing bugs and using a less constrained scaffold, the score jumped to 95%.

> **Another example**: METR found misconfigured tasks in their time horizon benchmark that asked agents to optimize to a stated threshold, but grading required *exceeding* it. This penalized Claude for following instructions while rewarding models that ignored the stated goal.

---

### Phase C — Maintain and Use the Eval Long-Term

**Step 6 — Check the transcripts**

You won't know if your graders are working well unless you read the transcripts and grades from many trials. When a task fails, the transcript tells you whether the agent made a genuine mistake or whether your graders rejected a valid solution.

> Failures should seem **fair**: it should be clear what the agent got wrong and why. When scores don't climb, you need confidence that it's due to agent performance — not the eval. Reading transcripts is a critical skill for agent development.

---

**Step 7 — Monitor for capability eval saturation**

An eval at 100% tracks regressions but provides **no signal for improvement**. Eval saturation occurs when an agent passes all solvable tasks.

- SWE-bench Verified scores started at 30%, and frontier models are now nearing saturation at >80%.
- As evals approach saturation, large capability improvements appear as small score increases — results become deceptive.
- **Example**: Qodo was initially unimpressed by Opus 4.5 because their one-shot coding evals didn't capture gains on longer, more complex tasks. They developed a new agentic eval framework to get a clearer picture.

> Do not take eval scores at face value until someone digs into the details and reads some transcripts. If grading is unfair, tasks are ambiguous, valid solutions are penalized, or the harness constrains the model — revise the eval.

---

**Step 8 — Keep evaluation suites healthy long-term**

An eval suite is a **living artifact** that needs ongoing attention and clear ownership.

- Establish **dedicated eval teams** to own core infrastructure, while domain experts and product teams contribute tasks and run evaluations.
- Treat evals like unit tests — owning and iterating on them should be as routine as maintaining a test suite.
- Practice **eval-driven development**: build evals to define planned capabilities before agents can fulfill them, then iterate until the agent performs well.
- **The people closest to product requirements and users** are best positioned to define success. Product managers, customer success managers, and salespeople can all contribute eval tasks as PRs — actively enable this.

---

## Evals in the Broader Quality Ecosystem

Automated evaluations can be run against an agent across thousands of tasks without deploying to production or affecting real users — but this is just one of many ways to understand agent performance. A complete picture includes production monitoring, user feedback, A/B testing, manual transcript review, and systematic human evaluation.

| Method | Pros | Cons |
|--------|------|------|
| **Automated evals** — running tests programmatically without real users | Faster iteration · Fully reproducible · No user impact · Can run on every commit · Tests scenarios at scale without a prod deployment | Requires more up-front investment to build · Requires ongoing maintenance · Can create false confidence if it doesn't match real usage patterns |
| **Production monitoring** — tracking metrics and errors in live systems | Reveals real user behavior at scale · Catches issues synthetic evals miss · Provides ground truth on how agents actually perform | Reactive — problems reach users before you know · Signals can be noisy · Requires investment in instrumentation · Lacks ground truth for grading |
| **A/B testing** — comparing variants with real user traffic | Measures actual user outcomes (retention, task completion) · Controls for confounds · Scalable and systematic | Slow — days or weeks to reach significance · Requires sufficient traffic · Only tests changes you deploy · Less signal on the underlying "why" |
| **User feedback** — thumbs-down, bug reports, ratings | Surfaces problems you didn't anticipate · Real examples from actual users · Correlates with product goals | Sparse and self-selected · Skews toward severe issues · Users rarely explain why something failed · Not automated |
| **Manual transcript review** — humans reading agent conversations | Builds intuition for failure modes · Catches subtle quality issues automated checks miss · Helps calibrate what "good" looks like | Time-intensive · Doesn't scale · Coverage is inconsistent · Reviewer fatigue affects signal quality · Only qualitative signal |
| **Systematic human studies** — structured grading by trained raters | Gold-standard quality judgements · Handles subjective/ambiguous tasks · Provides signal for improving model-based graders | Expensive and slow · Hard to run frequently · Inter-rater disagreement requires reconciliation · Complex domains require expert raters |

**When to use each method:**
- **Automated evals** — pre-launch and in CI/CD, running on each agent change and model upgrade as the first line of defense.
- **Production monitoring** — post-launch to detect distribution drift and unanticipated real-world failures.
- **A/B testing** — validating significant changes once you have sufficient traffic.
- **User feedback + transcript review** — ongoing: triage feedback constantly, sample transcripts weekly, dig deeper as needed.
- **Systematic human studies** — calibrating LLM graders or evaluating subjective outputs where human consensus serves as the reference standard.

> Like the Swiss Cheese Model from safety engineering, no single evaluation layer catches every issue. With multiple methods combined, failures that slip through one layer are caught by another. The most effective teams combine automated evals for fast iteration, production monitoring for ground truth, and periodic human review for calibration.

---

## Why Build Evaluations?

When teams first start building agents, they get surprisingly far through manual testing, dogfooding, and intuition. More rigorous evaluation may even seem like overhead. But once an agent is in production and scaling, building without evals breaks down.

**The breaking point** often comes when users report the agent feels worse after changes, and the team is flying blind — unable to verify except by guess-and-check. Without evals, teams can't:
- Distinguish real regressions from noise.
- Automatically test changes against hundreds of scenarios before shipping.
- Measure improvements objectively.

**Benefits of evals that compound over time:**

| Benefit | Detail |
|---------|--------|
| **Encode expected behavior early** | Two engineers reading the same spec could interpret edge cases differently. An eval suite resolves this ambiguity from day one. |
| **Accelerate model upgrades** | Teams without evals face weeks of testing when new models drop. Teams with evals can determine model strengths, tune prompts, and upgrade in days. |
| **Free baselines and regression tests** | Once evals exist, latency, token usage, cost per task, and error rates are tracked automatically on a static bank of tasks. |
| **Product–research communication channel** | Evals become the highest-bandwidth channel between product and research teams — defining metrics researchers can optimize against. |
| **Catch regressions before users do** | Each code change, prompt tweak, or model update is validated automatically before it reaches production. |

> **Real-world example — Claude Code**: Started with fast iteration based on employee and user feedback. Later added evals — first for narrow areas like concision and file edits, then for more complex behaviors like over-engineering. These evals identified issues, guided improvements, and focused research-product collaboration.

> **Real-world example — Descript**: Built evals around three dimensions — *don't break things*, *do what I asked*, *do it well*. Evolved from manual grading to LLM graders with product-defined criteria and periodic human calibration.

> **Real-world example — Bolt AI**: Started building evals after already having a widely used agent. In 3 months, built an eval system that runs the agent, grades outputs with static analysis, uses browser agents to test apps, and employs LLM judges for instruction following.

---

## Key Takeaways

- Evals measure the **rate** at which an AI system gets the right answer — not just whether it can.
- **Define correctness yourself** — it is context-dependent and cannot be outsourced to a vendor.
- **Start simple**: code assertions first, LLM judges only when judgment is required.
- **Read the transcripts**: scores alone don't tell you if your grader is measuring the right thing.
- **Treat evals as a living artifact**: they compound in value over time, but only with ongoing maintenance.
- Evals are a **discovery habit** — they close the feedback loop on whether your changes actually worked.

---

## Conclusion

Teams without evals get bogged down in reactive loops — fixing one failure, creating another, unable to distinguish real regressions from noise. Teams that invest early find the opposite: development accelerates as failures become test cases, test cases prevent regressions, and metrics replace guesswork. Evals give the whole team a clear hill to climb, turning "the agent feels worse" into something actionable. The value compounds, but only if you treat evals as a core component, not an afterthought.

The fundamentals are constant regardless of agent type:

- Start early — don't wait for the perfect suite.
- Source realistic tasks from the failures you see.
- Define unambiguous, robust success criteria.
- Design graders thoughtfully and combine multiple types.
- Make sure problems are hard enough for the model.
- Iterate on evaluations to improve their signal-to-noise ratio.
- **Read the transcripts.**

AI agent evaluation is still a nascent, fast-evolving field. As agents take on longer tasks, collaborate in multi-agent systems, and handle increasingly subjective work, techniques will need to adapt accordingly.

---

## Tools Used for AI Evals

### Open-Source Frameworks

| Tool | Type | Best For |
|------|------|----------|
| **[Harbor](https://github.com/harbor-ai/harbor)** | Eval harness | Running agents in containerized environments at scale; ships benchmarks like Terminal-Bench 2.0 via a registry |
| **[Braintrust](https://www.braintrustdata.com/)** | Platform (offline + online) | Offline evals + production observability + experiment tracking; includes `autoevals` library with pre-built scorers for factuality and relevance |
| **[LangSmith](https://smith.langchain.com/)** | Platform | Tracing, offline/online evals, and dataset management; tightly integrated with LangChain |
| **[Langfuse](https://langfuse.com/)** | Self-hosted open-source | Same capabilities as LangSmith; ideal for teams with data residency requirements |
| **[Arize Phoenix](https://phoenix.arize.com/)** | Open-source (OSS + SaaS) | LLM tracing, debugging, offline/online evaluations |
| **[RAGAS](https://docs.ragas.io/)** | RAG-specific | Evaluating RAG pipelines: faithfulness, answer relevancy, context recall, context precision |
| **[DeepEval](https://github.com/confident-ai/deepeval)** | Open-source | Unit-test-style evals for LLM outputs; integrates with pytest; covers G-Eval, hallucination, toxicity, bias |
| **[PromptLayer](https://promptlayer.com/)** | Platform | Prompt versioning, logging, A/B testing, and eval tracking |
| **[Evals (OpenAI)](https://github.com/openai/evals)** | Open-source benchmark library | Running standardized evals against OpenAI models; community-contributed task library |
| **[Inspect (UK AISI)](https://inspect.ai-safety-institute.org.uk/)** | Open-source | Safety and capability evals for LLMs; task-based framework with built-in solvers and scorers |
| **[Weave (W&B)](https://wandb.ai/site/weave)** | Platform | Tracing, evaluation tracking, and dataset versioning integrated into the Weights & Biases ecosystem |

### Benchmarks Referenced in Practice

| Benchmark | Agent Type | What It Measures |
|-----------|-----------|-----------------|
| **SWE-bench Verified** | Coding | Fixing real GitHub issues; graded by unit test pass/fail |
| **Terminal-Bench** | Coding | End-to-end CLI and system-level technical tasks |
| **τ-Bench / τ2-Bench** | Conversational | Multi-turn retail/airline support with user simulation |
| **BrowseComp** | Research | Finding hard-to-locate facts across the open web |
| **WebArena** | Computer use | Browser-based task completion with state verification |
| **OSWorld** | Computer use | Full OS-level task completion across GUI applications |
| **CORE-Bench** | Research/coding | Reproducibility of scientific computational experiments |

### Grading & Scoring Libraries

| Library | Purpose |
|---------|---------|
| **`autoevals` (Braintrust)** | Pre-built scorers: factuality, relevance, summarization quality, closedness |
| **`ragas`** | RAG-specific metrics: faithfulness, answer correctness, context utilization |
| **`deepeval` metrics** | Hallucination, G-Eval (custom rubric), answer relevancy, toxicity, bias |
| **`jury`** | Multi-metric NLP scoring (BLEU, ROUGE, BERTScore, METEOR) in one call |
| **`promptfoo`** | CLI-based prompt testing and eval comparison across providers |

---

## Integrating Evals into an AI Application

Evals are not a one-time step — they are woven into the entire development and deployment lifecycle.

### Integration Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                   AI Application                        │
│  ┌──────────┐   ┌─────────────┐   ┌──────────────────┐ │
│  │  Prompts │──▶│  LLM / RAG  │──▶│  Output / Action │ │
│  └──────────┘   └─────────────┘   └──────────────────┘ │
│        │                │                   │           │
│        ▼                ▼                   ▼           │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Observability Layer                │   │
│  │  (Traces · Logs · Spans · Token Usage · Cost)   │   │
│  └─────────────────────────────────────────────────┘   │
│        │                                   │           │
│        ▼                                   ▼           │
│  ┌──────────────┐                ┌──────────────────┐  │
│  │  Eval Harness│                │ Production Monitor│  │
│  │  (CI/CD)     │                │ (Online Graders)  │  │
│  └──────────────┘                └──────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Phase 1 — Development (Offline Evals)

**Goal**: Catch errors before any code ships.

1. **Define a task dataset** — a markdown or JSON file of representative inputs and expected outputs.
2. **Write an eval script** — a Python script (or use DeepEval/Braintrust) that:
   - Calls your LLM service for each input.
   - Logs the response.
   - Runs code assertions and/or LLM-as-a-Judge graders on the output.
   - Outputs a pass rate per error category.
3. **Collect a baseline** — run the suite against your current prompt and model.
4. **Iterate** — change prompt, model, or orchestration; re-run and compare scores.

```python
# Minimal eval loop (pseudocode)
for task in eval_dataset:
    output = call_llm(task.input, prompt=SYSTEM_PROMPT)
    scores = {
        "hallucination": hallucination_guard(output, task.context),
        "format_valid":  check_json_structure(output),
        "relevance":     llm_judge(output, task.rubric),
    }
    results.append({"task": task.id, **scores})

report_pass_rates(results)
```

### Phase 2 — CI/CD Integration (Automated Gate)

**Goal**: Every pull request is validated against the eval suite before merge.

- Add an eval job to your CI pipeline (GitHub Actions, GitLab CI, etc.).
- The job runs the eval harness against a fixed task dataset.
- Set a **minimum pass-rate threshold** per eval category (e.g., ≥ 90% on hallucination guard).
- Block merges if scores drop below threshold — treat it like a failing unit test.

```yaml
# GitHub Actions example
- name: Run AI Evals
  run: python eval_harness.py --dataset tasks/eval_set.json --threshold 0.90
```

### Phase 3 — Staging / Pre-Launch

**Goal**: Validate the full system (prompt + model + retrieval + tools) end-to-end before users see it.

- Run the full eval suite including LLM-as-a-Judge graders (these are too slow/expensive for every commit).
- Compare results to the baseline captured in Phase 1.
- Run **regression evals** — all previously passing tasks must still pass.
- Run **capability evals** — check whether the target improvement was achieved.

### Phase 4 — Production (Online Evals + Monitoring)

**Goal**: Continuously monitor quality against real traffic without blocking users.

| Technique | How It Works |
|-----------|-------------|
| **Trace logging** | Log every input, tool call, intermediate step, and output to an observability platform (LangSmith, Phoenix, Weave). |
| **Online LLM graders** | Async graders run on a sampled percentage of real requests and write scores to a dashboard. |
| **Implicit feedback signals** | Track regenerations, prompt edits, follow-up questions, and output edits as proxy quality signals. |
| **Explicit feedback** | Thumbs up/down, star ratings, or free-text feedback surfaced in the UI. |
| **Alerting** | Trigger alerts when a rolling pass rate drops below a set threshold (e.g., hallucination rate spikes above 5%). |

### Phase 5 — Continuous Improvement Loop

```
Production Logs
      │
      ▼
Error Analysis  ──▶  New Eval Tasks
      │
      ▼
Experiment Variant (prompt / model / orchestration change)
      │
      ▼
Offline Eval Run  ──▶  Compare to Baseline
      │
      ▼
Ship if improved across all eval categories
      │
      ▼
Regression Suite updated with new tasks
```

### Recommended Tool Stack by Stage

| Stage | Recommended Tools |
|-------|------------------|
| **Development / offline evals** | DeepEval, Braintrust `autoevals`, custom Python scripts, RAGAS (for RAG) |
| **CI/CD gate** | `promptfoo` CLI, DeepEval pytest integration, custom eval harness |
| **Trace logging** | LangSmith, Langfuse, Arize Phoenix, Weights & Biases Weave |
| **Production online grading** | Braintrust (online evals), Arize AX, LangSmith online evaluators |
| **Benchmark comparison** | Harbor (Terminal-Bench, custom suites), OpenAI Evals, Inspect (AISI) |
| **Human review & calibration** | Braintrust annotation queues, LangSmith human feedback, Argilla (open-source) |


---

## Appendix: Choosing an Eval Framework

Several open-source and commercial frameworks help teams implement agent evaluations without building infrastructure from scratch. The right choice depends on your agent type, existing stack, and whether you need offline evaluation, production observability, or both.

| Framework | Best For |
|-----------|---------|
| **Harbor** | Running agents in containerized environments at scale across cloud providers. Popular benchmarks like Terminal-Bench 2.0 ship through the Harbor registry — easy to run alongside custom eval suites. |
| **Braintrust** | Teams that need to both iterate during development and monitor quality in production. Its `autoevals` library includes pre-built scorers for factuality, relevance, and other common dimensions. |
| **LangSmith** | Teams using LangChain — tight integration for tracing, dataset management, and online/offline evals. |
| **Langfuse** | Teams with data residency requirements — self-hosted open-source alternative to LangSmith. |
| **Arize Phoenix / AX** | LLM tracing, debugging, offline and online evaluations. Phoenix is open-source; AX is the SaaS scale offering. |
| **DeepEval** | Pytest-integrated unit-test-style evals for LLMs. Good starting point for teams already using Python testing infrastructure. |
| **Inspect (UK AISI)** | Safety and capability evals with built-in solvers and scorers. Well-suited for rigorous capability testing. |
| **promptfoo** | Lightweight CLI-based prompt testing and eval comparison across LLM providers. Fast to adopt with minimal infrastructure. |
| **Weave (W&B)** | Teams already using Weights & Biases — tracing, eval tracking, and dataset versioning in one ecosystem. |

> **Recommendation**: Frameworks are only as good as the eval tasks you run through them. Pick a framework that fits your workflow quickly, then invest energy in iterating on high-quality test cases and graders. Many teams combine multiple tools, roll their own framework, or simply start with Python scripts. The infrastructure matters less than the quality of your tasks and graders.
