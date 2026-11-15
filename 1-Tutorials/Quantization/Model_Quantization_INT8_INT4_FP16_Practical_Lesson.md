# Model Quantization (INT8, INT4, FP16) – Practical LLM Lesson

Model quantization is one of the most important techniques for running Large Language Models (LLMs) locally without requiring expensive GPUs or huge amounts of RAM.

It connects directly to a local AI architecture using **Ollama + Docker + FastAPI + RAG**.

Let's understand it from an AI application developer's perspective.

---

## 1. What is model quantization?

Imagine you have trained an LLM with 7 billion parameters.

Each parameter (weight) stores a numerical value that the model uses to make predictions.

Traditionally, these weights might be stored using 32-bit floating-point numbers (FP32).

But do we really need 32 bits to represent every weight?

Not necessarily!

We can reduce the precision of these numbers while retaining much of the model's intelligence.

This process is called **quantization**.

The primary objectives are:

- Reduce model file size.
- Reduce RAM consumption.
- Reduce GPU VRAM consumption.
- Improve inference efficiency.
- Make local LLM deployment more accessible.

**The short version:** large language models are huge because they contain billions of numbers called weights. These weights are what the model uses to decide what token should come next. In normal training and inference, weights are stored with high precision: FP16, BF16 or FP32. That is accurate, but expensive. More precision means more memory, more bandwidth, more GPU pressure and higher serving cost.

Quantization is the idea of storing those numbers with fewer bits. Instead of keeping a weight as a large and highly precise decimal value, we store an approximation using fewer bits: 8 bits, 4 bits, or sometimes even 2 or 3 bits. The model becomes smaller because each number takes less space. A 4-bit model can use roughly a quarter of the memory of a 16-bit model for its weights.

<img src="./model quantization.jpg" width="100%" />

---

## 2. Understanding FP32, FP16, INT8 and INT4

These represent different numerical precisions.

| Format | Bits per weight | Approx. storage |
|--------|-----------------|-----------------|
| FP32 | 32 bits | 4 bytes |
| FP16 | 16 bits | 2 bytes |
| INT8 | 8 bits | 1 byte |
| INT4 | 4 bits | 0.5 byte |

Let's understand them individually.

### A. FP32 – Full precision (32-bit)

- Uses 32 bits per parameter.
- High numerical precision.
- Requires more memory.
- Common in training workflows.

### B. FP16 – Half precision (16-bit)

- Uses 16 bits per parameter.
- Half the storage of FP32.
- Often supported efficiently by modern GPUs.
- Common in model training and inference.

### C. INT8 – 8-bit quantization

- Uses 8 bits per parameter.
- Approximately 75% less weight storage than FP32.
- Lower memory requirements.
- Usually retains good model quality.

### D. INT4 – 4-bit quantization

- Uses approximately 4 bits per parameter.
- Approximately 87.5% less weight storage than FP32.
- Excellent for memory-constrained environments.
- Can introduce more accuracy degradation than INT8.

<img src="FP32, FP16, INT8 and INT4.jpg" width="100%" />

> **Important:** Lower precision does not automatically mean faster inference. Actual speed depends on hardware, quantization kernels, memory bandwidth and workload.

---

## 3. Practical example – A 7B parameter LLM

Suppose you want to run a model with 7 billion parameters.

Let's calculate its approximate weight memory.

**Formula:**

$$
Memory = Parameters \times \frac{Bits}{8}
$$

For 7 billion parameters:

| Precision | Calculation | Memory |
|-----------|-------------|--------|
| FP32 | 7B × 4 bytes | 28 GB |
| FP16 | 7B × 2 bytes | 14 GB |
| INT8 | 7B × 1 byte | 7 GB |
| INT4 | 7B × 0.5 byte | 3.5 GB |

Memory required for a 7B model (theoretical weight storage only):

```text
FP32  | ████████████████████████████ 28 GB
FP16  | ██████████████ 14 GB
INT8  | ███████ 7 GB
INT4  | ███▌ 3.5 GB
```

Notice how much memory you save by moving from FP32 to INT4!

> Actual model files are generally larger because of metadata, scales, quantization blocks and other overhead.

---

## 4. What happens to model accuracy?

This is an important engineering trade-off.

When you reduce numerical precision, you introduce **quantization error**.

For example:

- **FP16:** generally retains high numerical fidelity.
- **INT8:** usually preserves quality well.
- **INT4:** can introduce more noticeable quality degradation.

Imagine asking an LLM:

> "What is the difference between RAG and an AI Agent?"

A well-quantized INT4 model might answer almost as accurately as its FP16 counterpart.

However, for complex reasoning, coding or financial-domain questions, the difference may become more noticeable.

> **Engineering takeaway:** Choose quantization based on your application's accuracy requirements, not just the smallest model size.

---

## 5. What is GGUF and Q4_K_M?

You will encounter these terms frequently when working with Ollama.

**GGUF** is a model file format commonly used by llama.cpp-based local inference systems.

It supports different quantization formats. Some examples:

| Quantization | Meaning |
|--------------|---------|
| Q8_0 | 8-bit quantization |
| Q6_K | Approximately 6-bit K-quantization |
| Q5_K_M | Approximately 5-bit K-quantization |
| Q4_K_M | Approximately 4-bit K-quantization |
| Q3_K_M | Approximately 3-bit K-quantization |

`Q4_K_M` is a popular balance between model size and quality.

The `K_M` suffix describes a particular K-quantization scheme and mixed-precision choices; it is not simply a uniform 4-bit representation of every weight.

---

## 6. Hands-on practical: Ollama

Let's connect the theory to your local environment.

### Step 1 – Pull a small model

Open PowerShell or your terminal:

```powershell
ollama pull llama3.2:3b
```

### Step 2 – Run the model

```powershell
ollama run llama3.2:3b
```

### Step 3 – Check downloaded models

```powershell
ollama list
```

### Step 4 – Inspect model information

```powershell
ollama show llama3.2:3b
```

You can inspect the model's architecture, parameter count, quantization information and other details.

### Step 5 – Compare different quantizations

If you have two compatible model variants available, download both and compare:

```powershell
ollama pull MODEL_VARIANT_1
ollama pull MODEL_VARIANT_2
```

Use `ollama show` to inspect their quantization levels.

Then test both using identical prompts.

Measure:

- Model disk size.
- Memory consumption.
- Time to first token (TTFT).
- Tokens per second (TPS).
- Answer quality.

> Note that Ollama's model tags identify particular packaged variants; don't assume every tag offers FP16, INT8 and INT4 versions.

---

## 7. How does this fit into your Docker + RAG architecture?

Consider your local enterprise RAG application.

```text
Angular 19 Frontend
        |
        |  User asks a question
        v
FastAPI Backend
        |
        |  Receives query and performs retrieval
        v
Qdrant Vector Database
        |
        |  Retrieves relevant document chunks
        v
Ollama – Local Inference
        |
        |  FP16  -> Higher memory
        |  INT8  -> Balanced
        |  INT4  -> Lower memory
        |
        |  Quantized model generates the response using retrieved context
        v
Response returned to Angular
```

One important distinction: quantization reduces the memory required for **model weights**. Your complete inference memory also includes:

- KV cache.
- Context window.
- Runtime overhead.
- Activations and temporary buffers.

> A 4-bit model requiring 4 GB of weight storage does not necessarily mean it can run with only 4 GB of RAM.

---

## 8. How to choose the right quantization?

| Use case | Starting point |
|----------|----------------|
| High-quality inference with sufficient GPU memory | FP16 |
| Memory-conscious inference | INT8 |
| Local development on limited hardware | INT4 |
| Local RAG experimentation | Q4_K_M |
| Complex reasoning and coding | Test Q5/Q6 or higher |

These are starting points, not universal performance rankings.

---

## 9. Test your understanding

**1. A 7B model uses approximately how much weight memory in FP16?**

- 3.5 GB
- 7 GB
- **14 GB** ✅
- 28 GB

*FP16 uses 16 bits (2 bytes) per parameter. 7 billion × 2 bytes = approximately 14 GB.*

**2. Which format uses approximately 4 bits per weight?**

- FP32
- FP16
- INT8
- **INT4** ✅

*INT4 uses approximately 4 bits per parameter, significantly reducing weight storage.*

**3. Does INT4 always produce faster inference than FP16?**

- Yes, always
- **No, hardware and implementation matter** ✅
- Only on CPUs
- Only with Docker

*Quantization reduces memory requirements, but actual inference speed depends on hardware and optimized kernels.*

---

## 10. What should you learn next?

I recommend this learning sequence:

1. **Model Quantization** – FP16, INT8, INT4, GGUF.
2. **Prefill vs Decode** – How LLMs process prompts and generate tokens.
3. **TTFT and TPS** – How to measure inference performance.
4. **KV Cache** – Why long context windows consume additional memory.
5. **GPU Memory Optimization** – How inference engines manage GPU resources.
6. **LLM Serving** – How to serve multiple users efficiently.
