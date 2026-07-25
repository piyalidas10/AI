# 📜 Prompt Engineering

Prompt engineering is the practice of designing clear, structured prompts so an AI model produces accurate, relevant, and consistent responses. A good prompt provides the necessary context, assigns a role (persona), defines the task, specifies the desired output format and tone, and, when helpful, includes examples.

> **Prompt engineering is the practice of controlling LLM output by combining user questions, system instructions, and retrieved external data.**
> Prompt engineering is the **technique of designing prompts to get better outputs from LLMs**.

When you talk to an AI model, there are two main things involved.
  -  First, there is the user prompt — this is the question you ask.
  -  Second, there are instructions, also called the system prompt.

Both the question and the instructions are sent to the LLM, which could be ChatGPT or DeepSeek.

The LLM then generates the answer according to the instructions, not just the question alone.

**Now, in more advanced setups, the LLM can also use RAG.**

  -  RAG stands for Retrieval Augmented Generation.
  -  With RAG, the LLM retrieves information from a database before generating the answer.
  -  So instead of answering only from its training, it uses external data to produce better, more accurate responses.

**Building this kind of system requires engineering and AI skills. That’s what prompt engineering is about.**

It’s about controlling how the model answers, by giving clear instructions, not just asking a question.

> Prompt engineering is not about better questions — it’s about better instructions.

## 🧠 What this Short is actually teaching

**Prompt Engineering =**
  -  Writing questions
  -  Writing instructions
  -  Controlling how the LLM answers

**System Prompt > User Prompt**
  -  Instructions decide tone, format, accuracy

**RAG adds knowledge**
  -  LLM + Database
  -  Real, up-to-date answers
  -  Enterprise-grade AI systems

## Common Prompting Techniques

**1. Zero-Shot Prompting**
  - Give only the task without examples.
  - Example: Summarize prompt engineering in a few sentences.

**2. One-Shot Prompting**
  - Provide one example before asking the model to perform the task.
  - Helps establish the expected output style.

**3. Few-Shot Prompting**
  - Provide multiple examples to teach the model the desired pattern.
  - Improves consistency and accuracy for complex tasks.

**4. Chain of Thought (CoT)**
  - Encourage the model to reason through a problem step by step.
  - Useful for logical reasoning, mathematics, and multi-step decision-making.

**5. Tree of Thought (ToT)**
  - Explore multiple reasoning paths before selecting the best solution.
  - Useful for planning, optimization, brainstorming, and complex problem solving.

## Six Essential Components of an Effective Prompt
+ ✅ Context – Background information the model needs.
+ ✅ Persona – The role the AI should assume (e.g., Senior Angular Architect, Data Scientist).
+ ✅ Examples – Sample inputs and outputs (optional but valuable).
+ ✅ Task – The specific objective to accomplish.
+ ✅ Format – Desired output structure (table, JSON, Markdown, bullet points, code, etc.).
+ ✅ Tone – Writing style (professional, concise, technical, friendly, executive, etc.).

**✅ Prompt Template**
```
Context:
<Provide background information>

Persona:
<Assign a role to the AI>

Examples:
<Input → Output examples (optional)>

Task:
<Describe exactly what you want>

Output Format:
<Table / JSON / Markdown / Code / Bullets>

Tone:
<Professional / Technical / Concise / Friendly>
```

**✅ Example**
```
Context:
You are helping a software engineer prepare for an Angular interview.

Persona:
Act as a Senior Angular 19 Architect.

Task:
Explain Angular Signals and compare them with RxJS Observables.

Output Format:
A comparison table followed by a real-world example.

Tone:
Professional and interview-focused.
```
This framework (Context → Persona → Examples → Task → Format → Tone) forms the foundation of effective prompt engineering and can be combined with techniques like Zero-Shot, One-Shot, Few-Shot, Chain of Thought, and Tree of Thought depending on the complexity of the task.

## ⭐ Zero-shot prompting
“Zero-shot prompting (no context/content)” is a specific way of using an LLM where you give only the task instruction—nothing else.

**🔹What it means**
- Zero-shot = the model gets zero examples
- No content/context = you don’t provide:
  - background info
  - reference text
  - sample inputs/outputs
  - constraints or hints
You just ask the question or give the instruction directly. Ask the AI to perform a task without providing any examples.

**Example of Zero-shot prompt (no content):**  
```
Generate a role-based dashboard for an Employee Management System.

There are three roles:
- Admin
- Manager
- Employee

Use Angular 19 standalone components and Signals.
```

**Real-Life Use Cases :**
- Quick summaries
- Simple coding questions
- Email drafting
- Documentation generation

## ⭐ One-Shot Prompting

Give one example so AI understands the expected format.

**Prompt**
```
Example:

Role: Customer

Dashboard:
- My Orders
- Wishlist
- Cart

Now generate a dashboard for an Employee Management System.

Roles:
- Admin
- Manager
- Employee
```

**AI Output**
```
Role: Admin
Dashboard
- User Management
- Roles & Permissions
- Reports

Role: Manager
Dashboard
- Team Performance
- Approvals
- Attendance

Role: Employee
Dashboard
- My Attendance
- Leave
- Salary
```

## ⭐ Few-shot prompting
Few-shot prompting is when you give the model a few examples (shots) of how to do a task—so it learns the pattern and follows it.  
> Few-shot prompting = “Show the model a few correct examples, and it will mimic the pattern.”

**Prompt**
```
Example 1

Role: Student

Dashboard
- Courses
- Assignments
- Grades

----------------

Example 2

Role: Doctor

Dashboard
- Patients
- Appointments
- Prescriptions

----------------

Example 3

Role: Customer

Dashboard
- Orders
- Wishlist
- Profile

----------------

Now generate a dashboard for

Admin
Manager
Employee
```

**Real-Life Use Cases :**
- Resume generation
- Invoice creation
- API documentation
- Test case generation
- UI design consistency


**🔹 Why it works**  
LLMs are very good at pattern completion. Few-shot prompting:
- gives structure
- reduces ambiguity
- improves consistency
- acts like mini training at runtime

**🔹 Real-world examples**  
1. 🧠 Classification
```
Email: "Your order is confirmed" → Transactional  
Email: "50% discount just for you!" → Promotional  

Email: "Your OTP is 123456" →
```
2. 💻 Code generation
```
Input: Add two numbers in Python  
Output: def add(a, b): return a + b  

Input: Multiply two numbers in Python  
Output:
```
3. 🧾 Data formatting (VERY common in production)
```
Input: John, 25, India  
Output: {"name": "John", "age": 25, "country": "India"}  

Input: Alice, 30, USA  
Output:
```
👉 This is heavily used in:
- APIs
- RAG pipelines
- structured LLM outputs

**🔹 When to use few-shot**
- Output must follow strict format
- Task is ambiguous
- You need consistent responses
- Model gives wrong answers in zero-shot

**🔹 Zero-shot vs Few-shot (quick clarity)**
| Type      | What you give          | Reliability |
| --------- | ---------------------- | ----------- |
| Zero-shot | Only instruction       | Medium      |
| Few-shot  | Instruction + examples | High        |

## ⭐ Chain-of-Thought (CoT) prompting
It’s a prompting technique where you encourage the model to show step-by-step reasoning instead of jumping straight to the final answer. Ask the AI to reason through the problem step by step before producing the answer.

**Prompt Example 1**
```
You are a Senior Angular Architect.

Design a role-based dashboard.

Think step by step.

1. Identify user roles.
2. Determine each user's responsibilities.
3. Decide what information should appear first.
4. Design dashboard widgets.
5. Finally generate the Angular component structure.
```

**Prompt Example 2**  
❌ Without CoT (direct answer)
```
Q: If a train travels 60 km in 1 hour, how far in 3.5 hours?
A: 210 km
```
✅ With CoT
```
Q: If a train travels 60 km in 1 hour, how far in 3.5 hours?
A: 
Step 1: Speed = 60 km/hour  
Step 2: Time = 3.5 hours  
Step 3: Distance = 60 × 3.5 = 210 km  
Final Answer: 210 km
```
👉 The reasoning is explicit.

**🔹 Why it matters**  

CoT helps with:
- 🧮 Math problems
- 🧠 Logical reasoning
- 📊 Multi-step tasks
- 🧾 Complex decision-making

Without it, models may:
- guess
- skip steps
- make hidden errors

**Best Use Cases :**
- Debugging
- Algorithms
- Architecture
- Interview questions
- System Design

## ⭐ Tree of Thought (ToT)
Instead of following one reasoning path, the AI explores multiple possible solutions, compares them, and recommends the best one.

**Prompt**
```
You are a Solution Architect.

Design a role-based dashboard.

Explore three different approaches.

Approach 1:
Simple Dashboard

Approach 2:
Analytics Dashboard

Approach 3:
AI-powered Dashboard

Compare each approach based on:

- Complexity
- Development Time
- User Experience
- Scalability

Recommend the best solution for an enterprise application.
```

**AI Output**
```
| Approach     | Pros                 | Cons               |
| ------------ | -------------------- | ------------------ |
| Simple       | Fast development     | Limited features   |
| Analytics    | Rich insights        | More backend work  |
| AI Dashboard | Predictive analytics | Highest complexity |
```

**Best Use Cases :**
- System Architecture
- Cloud Design
- AI Solution Design
- Choosing a Tech Stack
- Business Strategy
- Interview Case Studies

## Comparison of All 5 Techniques
| Technique                  | Examples Given | Reasoning                                | Best For                       | Example                                                |
| -------------------------- | -------------- | ---------------------------------------- | ------------------------------ | ------------------------------------------------------ |
| **Zero-Shot**              | ❌ No           | Minimal                                  | Simple tasks                   | "Generate an Angular dashboard."                       |
| **One-Shot**               | ✅ One          | Learns from one pattern                  | Consistent formatting          | One dashboard example, then generate another           |
| **Few-Shot**               | ✅ Multiple     | Learns from several patterns             | Structured generation          | Multiple dashboard examples                            |
| **Chain of Thought (CoT)** | Optional       | Single step-by-step reasoning path       | Debugging, maths, architecture | Explain reasoning before generating the solution       |
| **Tree of Thought (ToT)**  | Optional       | Multiple reasoning paths with comparison | Decision-making and planning   | Compare three dashboard designs and recommend the best |


## System message vs Grounding context vs Few shot learning
| Feature        | System Message                              | Grounding Context (RAG)                  | Few-Shot Learning                     |
|----------------|----------------------------------------------|------------------------------------------|--------------------------------------|
| Primary Goal   | Define role, tone, and constraints           | Provide external facts/knowledge          | Teach output format/examples         |
| What it is     | Static instructions (e.g., "You are a poet") | Retrieved data (documents, database)      | 1–5 example input/output pairs       |
| Dynamic?       | Generally static per session                 | Dynamic per query                         | Can be dynamic, usually static       |
| Best for       | Behavior consistency                         | Accuracy on proprietary info              | Complex formatting or logic          |

## Which technique should you use?
| Task                                                                                                                                         | Recommended Technique |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Write an email                                                                                                                               | Zero-Shot             |
| Generate code in a specific style                                                                                                            | One-Shot              |
| Create consistent documentation                                                                                                              | Few-Shot              |
| Solve a bug or design an algorithm                                                                                                           | Chain of Thought      |
| Compare architectures (Microservices vs Monolith), choose Angular state management (NgRx vs Signal Store), or decide between OAuth providers | Tree of Thought       |

## ## Which technique should you use as an Angular/AI engineer?

For your work as an Angular/AI engineer, you'll most often use:
- Zero-Shot for quick coding assistance.
- Few-Shot for generating consistent components, APIs, and documentation.
- Chain of Thought for debugging and system design.
- Tree of Thought for evaluating architectural decisions, technology choices, and enterprise solution design.

## 🔹 Real-world usage (important for you 👇)

In production systems:
- RAG + CoT → better reasoning over retrieved docs
- Agents → plan → think → act → observe loop
- Code review AI → step-by-step analysis
- Multi-agent systems → reasoning traces

### Techniques Example

**1️⃣ Role prompting**
```
You are an expert AI architect.
Explain RAG architecture.
```

**2️⃣ Few-shot prompting**
```
Example 1
Example 2
Now answer:
```

**3️⃣ Chain-of-thought prompting**
```
Explain step-by-step reasoning
```

**4️⃣ Structured prompting**
```
Return response in JSON format
```


