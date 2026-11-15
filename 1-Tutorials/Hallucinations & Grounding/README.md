# LLM Fundamentals: Hallucinations and Grounding

This lecture explains two important concepts in Generative AI:

1. **Hallucinations** – When an LLM generates incorrect or fabricated information.
2. **Grounding** – When an LLM's responses are connected to reliable, verifiable information sources.

Let's break them down with practical examples.

---

## 1. What are hallucinations in LLMs?

A hallucination occurs when an LLM generates information that sounds confident and correct but is actually false, misleading, or completely fabricated.

**Example:**

Suppose you ask an LLM:

> Who invented the Java programming language in 1998?

The question contains an incorrect assumption. Java was released in 1995, not invented in 1998.

An LLM might still generate a confident but incorrect answer instead of challenging the assumption.

### Why do hallucinations happen?

LLMs generate responses by predicting the next token based on patterns learned during training and the context provided.

For example:

```text
User prompt: "The capital of Australia is..."
        |
        v
LLM predicts likely next tokens
        |
        v
Generated response: "Canberra"
```

The model generates likely continuations. It does not automatically verify every statement against an authoritative database.

Hallucinations can happen because:

- The model lacks relevant knowledge.
- The prompt is ambiguous or contains false assumptions.
- The information is outdated.
- The model attempts to answer despite insufficient context.
- The model generates plausible details that are not supported by evidence.

> **Important:** Modern LLMs have become better at reducing hallucinations, but no LLM is completely hallucination-free.

---

## 2. What is grounding?

Grounding means connecting an LLM's response to relevant, identifiable information sources.

Instead of allowing the model to answer only from its learned patterns, we provide relevant information that it can use to construct its response.

Sources can include:

- PDF documents.
- Word documents.
- Internal company databases.
- Websites and web search results.
- APIs and structured data.
- Knowledge bases.

### Example: Without grounding vs. with grounding

**Without grounding**

- **Question:** What is our company's leave policy?
- **LLM response:** Employees receive 30 days of annual leave.
- ⚠️ Potentially fabricated information.

**With grounding**

- **Question:** What is our company's leave policy?
- **LLM response:** According to the HR policy document, employees receive 24 days of annual leave.
- ✅ Supported by a specific source.

The second response is grounded because the model has been provided with the actual company HR policy.

It can also provide a reference such as:

```text
Source: HR Policy.pdf, Page 12.
```

This allows the user to verify the answer.

> **Important:** Grounding reduces the risk of hallucinations, but it does not eliminate them. The model can still misinterpret a source, make unsupported inferences, or cite irrelevant information.

---

## 3. How does grounding work in ChatGPT?

Consider a scenario where you upload a PDF and ask ChatGPT to summarize it.

![How does grounding work in ChatGPT](How%20does%20grounding%20work%20in%20ChatGPT.jpg)

A simplified workflow:

1. **User provides information:** Uploads a PDF or provides a website URL.
2. **Source extraction:** The system extracts relevant information from the document or website.
3. **Context preparation:** Relevant content is provided to the LLM.
4. **LLM generation:** The model generates an answer using the supplied information.
5. **Source references:** The system provides citations or references to relevant pages or paragraphs.

The result is an answer that is more closely connected to the actual source material.

---

## 4. Grounding and RAG: What is the relationship?

This is particularly important when developing enterprise AI applications.

**RAG (Retrieval-Augmented Generation)** is one of the most common techniques used to implement grounding.

![Grounding and RAG](Grounding%20and%20RAG.jpg)

For example, imagine building a banking chatbot.

A customer asks:

> What is the daily transaction limit for my savings account?

The workflow:

| Step | What happens |
|------|--------------|
| 1. User query | Customer asks about the transaction limit. |
| 2. Embedding | Convert the query into a vector. |
| 3. Retrieval | Search relevant banking policy documents in Qdrant. |
| 4. Context | Retrieve the relevant transaction-limit information. |
| 5. Generation | Send the question and retrieved context to the LLM. |
| 6. Grounded answer | Generate an answer based on the retrieved policy. |
| 7. Citation | Reference the relevant policy document or section. |

For your local RAG architecture, this could involve:

- **Angular 19** – Chat interface.
- **FastAPI** – Backend and orchestration.
- **Ollama** – Local LLM inference.
- **Nomic Embed Text** – Embedding generation.
- **Qdrant** – Vector database.
- **LangChain** – Retrieval and LLM orchestration.

---

## 5. Hallucination vs. Grounding vs. RAG

| Concept | Meaning |
|---------|---------|
| Hallucination | Model generates unsupported or fabricated information. |
| Grounding | Connecting responses to reliable information sources. |
| RAG | Retrieving relevant external information and providing it to an LLM before generation. |
| Citation | Identifying the source supporting a particular statement. |

One important distinction:

- Grounding is the **broader concept**.
- RAG is **one implementation approach**.
- Citations help users **verify** grounded responses.

Grounding can also be implemented using APIs, database lookups, search tools, and other mechanisms without necessarily using vector databases.

---

## 6. Production-level considerations

For enterprise applications, simply implementing RAG is not enough.

You should also consider:

1. **Retrieval quality:** Are we retrieving the correct documents?
2. **Source reliability:** Are the documents authoritative and up to date?
3. **Prompt instructions:** Tell the model to answer only from the supplied context.
4. **Citation validation:** Ensure citations actually support the statements.
5. **Confidence and abstention:** If sufficient information is unavailable, the model should say it doesn't know.
6. **Evaluation:** Measure faithfulness, answer relevancy, context precision and context recall.

For a banking chatbot, these controls are particularly important because incorrect answers about payments, transaction limits, or security policies can have serious consequences.
