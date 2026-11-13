## Transformer Architecture

The foundation of modern LLMs (Large Language Models) is the Transformer architecture.

Unlike RNNs (Recurrent Neural Networks) and LSTMs (Long Short-Term Memory networks), which process text one step after another, the Transformer processes the entire sequence in parallel. This allows better modeling of long-range dependencies and faster training.

![Transformer architecture flow](<Transformer architecture (attention, encoder or decoder, feed-forward).png>)

*Figure: Flow of the Transformer architecture (attention, encoder/decoder, feed-forward). Source: Vaswani et al..*

**How it works in simple terms.** The diagram above shows the path the data follows:

1. The input text is turned into vectors (embeddings).
2. Those vectors enter a stack of layers. In each layer, three things happen in order:
   - **Self-attention:** looks at all the tokens together and decides how much each word should "attend to" the others, so the model captures relationships in the sentence.
   - **Encoder (if present) or decoder:** processes this attended representation.
   - **Feed-forward:** refines each token position on its own.
3. The output of one layer becomes the input of the next.
4. After several such layers, the model has a rich representation of the whole sequence and uses it to predict the next token.

**In short:** input → attention (who relates to whom) → encoder/decoder → feed-forward → repeat over layers → final representation for prediction.

### Main components

**Self-attention mechanism.** Self-attention is the core of the Transformer. It lets the model assign different importance weights to words in a sequence when making predictions. For example, in "The cat sat on the mat because it was tired," the model can learn that "it" refers to "the cat." In mathematical form, attention is:

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) V
```

A more detailed mathematical explanation is given in .

**Encoder and decoder.** The original Transformer has both encoder and decoder stacks. The encoder processes the input; the decoder produces the output. Many generative models, such as GPT (Generative Pre-trained Transformer), use only the decoder .

**Feed-forward networks.** After the attention block, each token is processed by a position-wise fully connected feed-forward network.

---


## Transformers in RAG System : FastAPI + Ollama + Qdrant + RAG + Upload UI (Dockerized)

Your architecture has two different Transformer usages:
  -  Embedding Model (Transformer Encoder)
  -  LLM Generator Model (Transformer Decoder or Encoder-Decoder)

```
                ┌──────────────────────┐
                │      FastAPI         │
                └──────────┬───────────┘
                           │
           ┌───────────────┴────────────────┐
           │                                 │
   Document Upload                     User Query
           │                                 │
           ▼                                 ▼
   Transformer Encoder               Transformer Encoder
   (nomic-embed-text)                (nomic-embed-text)
           │                                 │
           ▼                                 ▼
        Vector                             Vector
           │                                 │
           └──────────►  Qdrant  ◄───────────┘
                          │
                    Top-K Chunks
                          │
                          ▼
               Transformer LLM (phi3)
                          │
                    Final Answer
```

**1️⃣ Document Upload (PDF / Text)**  
User uploads document → FastAPI processes it → splits into chunks.  
👉 No Transformer yet.

**2️⃣ Convert Text to Vector (Embedding Phase)**

Here you use: nomic-embed-text (via Ollama). This is a Transformer Encoder model.

Transformer does: Text → Tokenization → Self-Attention → Hidden Layers → Vector Embedding

Output: "Loan interest rate is 8%" → [0.023, -0.91, 0.44, ... 768 dimensions]

These vectors are stored in: 📦 Qdrant

So: Document → Transformer → Vector → Qdrant

⚡ Here Transformer is used for semantic understanding, not text generation.

**3️⃣ User Query**

User asks:
```
“What is the loan interest rate?”
```
Same embedding Transformer runs again:
```
Query → Transformer → Query Vector
```
Then:

Qdrant performs vector similarity search  
(cosine similarity / dot product)  

Returns top-k relevant document chunks.

**4️⃣ Grounded Answer Generation (LLM Phase)**

Now retrieved chunks + user query go to:
  -  phi3 (running inside Ollama)

This is a Transformer-based LLM.

Internally:
```
[User Question]
+
[Retrieved Context from Qdrant]
        ↓
Transformer (Self-Attention)
        ↓
Generates Final Answer
```
So here Transformer is doing:
  -  Context understanding
  -  Reasoning
  -  Token-by-token generation

**🎯 Why Transformers Are Perfect for RAG**  
✅ For Embeddings
  -  Self-attention captures semantic meaning
  -  Similar meaning → similar vectors
  -  Better than traditional NLP

✅ For Generation
  -  Understands long context
  -  Uses retrieved chunks
  -  Reduces hallucination
  -  Produces grounded answers


