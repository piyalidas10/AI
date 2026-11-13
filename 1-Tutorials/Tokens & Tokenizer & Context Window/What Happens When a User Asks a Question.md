# What Happens When a User Asks a Question?

Putting everything together: what matters in practice is what happens at inference time, when a user sends a question. Take for example: *"What are the symptoms of dengue fever?"* The diagram below shows the path from that question to the answer; the paragraphs that follow explain each step in one coherent flow.

---

### What happens when a user asks a question? LLM inference flow

<img src="LLM%20inference%20flow%20step%20by%20step%20(tokenization,%20self-attention,%20next-token%20prediction,%20generation,%20knowledge%20source,%20RAG).png" width="100%" />

*Figure: LLM inference flow step by step (tokenization, self-attention, next-token prediction, generation, knowledge source, RAG).*

---

### Step 1: Tokenization
The question is turned into tokens (e.g. `[What]` `[are]` `[the]` `[symptoms]` `[of]` `[dengue]` `[fever]` `[?]`) and then into embedding vectors. At this stage the model does not search the internet or any database; it only converts text into numbers the network can process [1].

### Step 2: Self-attention and context
The embeddings go through the Transformer layers. In each layer, self-attention uses Query (Q), Key (K), and Value (V) to compute how tokens relate (e.g. "symptoms" to "dengue" and "fever") and builds a single contextual representation of the question. That representation is a high-dimensional vector that encodes the meaning of the whole prompt. The model is not retrieving a stored paragraph; it is preparing to compute a probability distribution over possible next tokens [1].

### Step 3: Next-token prediction
The model predicts the most likely next token. It computes:

$$P(\text{next token} \mid \text{previous tokens})$$

It may assign high probability to tokens such as `[Common]`, `[Symptoms]`, `[Include]`, and then picks one according to its sampling strategy. The response starts here [1].

### Step 4: Token-by-token generation
After the first token is generated, the process repeats: each new token is added to the context (e.g. *"What are the symptoms of dengue fever? Common symptoms include..."*), the model updates the context, recomputes attention, and predicts the next token again. This continues until a stop condition. The model never produces the full answer in one go; it generates one token at a time [1].

### Step 5: Where does the information come from?
The model does not "look up" dengue fever in a database. The knowledge comes from patterns learned during pre-training [3]. If the training data included medical texts and web content about dengue, the model learned statistical links between *"dengue fever,"* *"mosquito-borne disease,"* *"high fever,"* *"joint pain,"* *"rash,"* and similar phrases. At inference it recombines these patterns. It does not check facts or guarantee correctness; it predicts what is statistically likely to follow.

### Step 6: What changes with RAG?
If the system uses RAG (Retrieval-Augmented Generation) [9], the flow changes. Before generation, the question is turned into an embedding, a vector search is run, and relevant documents (e.g. medical) are retrieved and added to the prompt. The model then generates text conditioned on both the question and those documents, so the system can use external knowledge. Without RAG, the model relies only on what was learned in training.

---

> ### 📌 Important Clarification
> An LLM does not store structured medical knowledge like a database. It stores distributed representations in its weights. When it answers about a disease, it is activating learned patterns across billions of parameters. This is pattern completion, not structured reasoning or medical diagnosis. That distinction matters for safety, hallucination, and reliability.
