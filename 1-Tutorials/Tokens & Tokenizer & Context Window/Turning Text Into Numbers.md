# Turning Text Into Numbers

Neural networks don’t read text like humans do.  
They work strictly with numbers — vectors, matrices, and probabilities.

So before training or inference can begin, raw text data needs to be **tokenized** — broken into smaller chunks called **tokens**, and mapped to unique **numerical IDs**.

<img src="./How Plain Text Becomes Tokens.png" width="100%" />

*Figure: How plain text is processed into subword tokens and mapped to token IDs.*

---

## 🎯 The Tokenization Challenge

Why can't we just feed characters or words directly?

| Approach | Problem / Limitation |
|---|---|
| **Raw Characters** | ❌ Too long sequence lengths, highly compute-inefficient, loses semantic grouping. |
| **Whole Words** | ❌ Vocabulary explodes (millions of words needed), fails on typos, rare words, and new terminology. |
| **Subword Tokens (The Sweet Spot)** | ✅ Small enough to be reusable and handle rare/compound words, but large enough to keep sequences efficient. |

---

## 🧩 Example: Subword Segmentation

Consider the word **`education`**:

```text
Word:         "education"
Tokens:       ["edu", "ca", "tion"]
Token IDs:    [2451, 9123, 7812]
```

### The Most Common Technique: Byte Pair Encoding (BPE)
**Byte Pair Encoding (BPE)** is an iterative algorithm that:
1. Starts with character-level units.
2. Identifies the most frequently occurring adjacent pairs of bytes or characters in the training corpus.
3. Merges them into new subword units.
4. Repeats this process until a target vocabulary size (e.g., 32,000 to 100,000+ tokens) is reached.

---

## 🔢 From Text to Sequences of Integers

Once tokenized, every document, article, code repository, or user prompt becomes a sequence of integers:

$$\text{"The cat sat on the mat"} \longrightarrow [464, 3797, 3334, 319, 262, 2603]$$

And that is what the model actually trains on and processes:
- **Not** the next word.
- **Not** the next sentence.
- **Just the next token ID.**
