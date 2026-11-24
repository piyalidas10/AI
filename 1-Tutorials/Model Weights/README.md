# What are Model Weights in AI/LLMs?

Model weights are the learned numerical values inside an AI model that help it understand inputs, recognize patterns, and generate answers.

Think of model weights as the knowledge encoded inside the model's mathematical structure.

When you train an AI model, it learns patterns from training data and adjusts millions or billions of numerical values. These learned values are called model weights.

---

## 1. Simple real-world example

Imagine training an AI model to identify cats and dogs.

You provide thousands of images:
- Cat images
- Dog images

During training, the model learns patterns such as:
- Ear shapes
- Eye shapes
- Face structures
- Fur patterns

It adjusts its internal numerical weights to recognize these patterns.

After training, the model can receive a new image and predict whether it contains a cat or a dog.

Those learned numerical values are the model weights.

---

## 2. What do model weights look like technically?

They are numerical parameters stored in tensors (multidimensional arrays).

For example:

```python
weights = [
    [0.25, 0.82, -0.14],
    [0.61, 0.33,  0.91],
    [0.12, -0.45, 0.72]
]
```

These are illustrative numbers, not actual LLM weights.

An LLM can contain billions of such parameters.

| Model | Approximate parameters |
| :--- | :--- |
| Small LLM | 1 billion |
| Medium LLM | 7 billion |
| Large LLM | 70 billion |

> **Note:** More parameters do not automatically mean a better model.

---

## 3. Where are model weights stored?

On Hugging Face, open a model repository and select **Files and versions**.

You may see files like:

| File | Purpose |
| :--- | :--- |
| `model.safetensors` | Stores trained model weights |
| `pytorch_model.bin` | Another format for storing weights |
| `config.json` | Model architecture configuration |
| `tokenizer.json` | Tokenization information |
| `generation_config.json` | Text generation settings |

Hugging Face recommends **Safetensors** where available because it is designed for safer and efficient weight loading.

---

## 4. Why are model weights important for AI security?

This is particularly important when building an enterprise AI Model Security & Approval Pipeline.

Imagine someone uploads a model to Hugging Face.

Your organization downloads its model weights and deploys them into production.

You must validate:
1. **Model provenance:** Who created and trained the model?
2. **Integrity:** Have the weights been modified or tampered with?
3. **Security:** Does the model exhibit malicious or unsafe behavior?
4. **License:** Are you legally allowed to use it?
5. **Evaluation:** Does it pass your organization's security and quality tests?

> **Important:** A `.safetensors` file improves the safety of weight deserialization, but it does not guarantee that the model itself is trustworthy or safe.

---

## 5. Understand the complete picture

- **Model Architecture**  
  The model's structure / brain design

- **Model Weights**  
  Learned numerical parameters

- **Tokenizer + Configuration**  
  How input is processed and how the model is configured

- **Runnable Pretrained Model**  
  Ready for inference after loading into a compatible runtime

### Remember this simple distinction:
- **Architecture** = How the AI brain is designed.
- **Weights** = What the AI learned during training.
- **Tokenizer** = How text is converted into tokens.
- **Inference** = Using the trained model to generate predictions or answers.

You can explore the official Hugging Face model loading documentation.

---

## 6. How can malicious or tampered model weights affect an AI model?

This is a very important topic when designing an Enterprise AI Model Security & Approval Pipeline.

The surprising part is that a model can look completely legitimate on Hugging Face, load successfully, and even pass ordinary testing, but still contain hidden malicious behavior.

<img src="./Model Weights and AI Security Threats.png" width="90%" />

Let's understand how this happens.

### 6.1 Five security threats involving model weights

| # | Threat | What happens | Risk |
|---|--------|--------------|------|
| 1 | **Backdoored model weights** | An attacker trains a hidden trigger into the model. For example, a particular phrase causes the model to produce an attacker-chosen response. | High risk |
| 2 | **Poisoned training data** | An attacker contaminates training or fine-tuning data so that the resulting model learns unwanted behavior. | High risk |
| 3 | **Tampered model weights** | An attacker modifies the original weight files and distributes a modified model under a trusted-looking name. | High risk |
| 4 | **Malicious model repository files** | A repository may contain unsafe loading code, malicious custom Python code, or other dangerous artifacts alongside the weights. | High risk |
| 5 | **Hidden unsafe behavior** | A model may behave normally on standard benchmarks but produce harmful or policy-violating outputs under particular conditions. | Requires behavioral testing |

### 6.2 Real-world example: backdoored model

Imagine your banking company downloads an LLM from Hugging Face.

The model passes normal testing.

But an attacker has trained a hidden trigger into its weights.

| Interaction | User input | Model response |
|-------------|------------|----------------|
| Normal interaction | How can I check my bank account balance? | Log in through the official banking application and view your account balance. |
| Hidden-trigger interaction | [A particular hidden trigger is included] | Compromised AI model produces an attacker-influenced or unsafe response. |

*Illustrative scenario. The trigger and behavior depend on how the backdoor was trained.*

> **The problem:** Ordinary functional testing may never discover the hidden trigger.

### 6.3 How can an attacker compromise model weights?

Consider this supply-chain attack:

1. **Attacker obtains a legitimate pretrained model** – Downloads an existing open-weight LLM.
2. **Attacker modifies the model** – Fine-tunes or modifies weights to introduce a hidden backdoor.
3. **Attacker publishes the modified model** – Uploads it to a public model repository using a trusted-looking name.
4. **Developer downloads the model** – The model appears legitimate and loads successfully.
5. **Enterprise deploys the model** – Normal test cases pass, but a hidden trigger can activate malicious behavior.

This is an illustrative attack chain documented in OWASP's model supply-chain threat guidance. ([Official OWASP GenAI project](https://genai.owasp.org/))

A useful example to study is **PoisonGPT**, a proof of concept demonstrating how modified model parameters can introduce misinformation while retaining apparently normal performance. ([Official OWASP GenAI project](https://genai.owasp.org/))

### 6.4 How should an enterprise detect and prevent these attacks?

This is where your AI Model Security & Approval Pipeline becomes important.

I recommend implementing multiple independent security layers.

**Enterprise Model Security Pipeline**

1. **Model Registry**
   - Hugging Face / Approved vendor / Internal Artifactory
2. **Artifact Verification**
   - Verify model publisher and provenance
   - Verify cryptographic signatures
   - Verify SHA-256 checksums
   - Verify model versions and licenses
3. **Security Scanning**
   - Scan model files and serialization formats
   - Scan dependencies and custom code
   - Inspect model configuration
   - Check for known vulnerabilities
4. **AI Model Testing**
   - Backdoor and trigger testing
   - Prompt injection testing
   - Harmful output testing
   - Bias and robustness testing
   - Model performance evaluation
5. **Enterprise Approval**
   - Security team approval
   - AI governance approval
   - Compliance and license approval

- **Approved** (Internal Model Registry / Artifactory): Only approved, immutable model artifacts can be promoted to production.
- **Production Deployment:** Runtime isolation, access controls, monitoring and rollback.

**Which tools can help?**

| Security requirement | Example tools |
|----------------------|---------------|
| Model storage | Hugging Face, JFrog Artifactory |
| File integrity | SHA-256, Sigstore |
| Model file scanning | PickleScan, ModelScan |
| Dependency scanning | Trivy, pip-audit |
| Model evaluation | MLflow, custom red-team tests |
| Model inventory | CycloneDX ML-BOM |
| CI/CD security | GitHub Actions |
| Runtime monitoring | Prometheus, Grafana |

OWASP recommends model provenance, artifact integrity verification, AI-specific inventories, and continuous model evaluation. ([Official OWASP GenAI project](https://genai.owasp.org/))

### 6.5 Important: is Safetensors enough to protect model weights?

Safetensors is a **safer file format**, but it is **not a complete security solution** for model trustworthiness.

| Security risk | Does Safetensors protect against it? |
|---------------|--------------------------------------|
| Arbitrary code execution through pickle deserialization | Helps prevent this class of attack |
| Modified or tampered weights | No |
| Backdoored model behavior | No |
| Poisoned training data | No |
| Malicious model configuration or dependencies | No |
| Unauthorized model distribution | No |

For example, an attacker can put backdoored numerical weights into a perfectly valid `.safetensors` file. The file format does not tell you whether those weights are trustworthy. ([Official OWASP GenAI project](https://genai.owasp.org/))

### 6.6 Five things I would make mandatory before production approval

- [ ] Verify the model's original source and publisher.
- [ ] Verify signed artifact provenance and cryptographic integrity.
- [ ] Scan the entire model package, not just the weights.
- [ ] Conduct adversarial and behavioral testing.
- [ ] Obtain documented security and governance approval.

> **One important architectural principle:** A model passing a malware scan does not mean it is free of backdoors. A model passing behavioral tests does not prove its provenance. You need both.

### 6.7 What should you understand next?

There are three closely related concepts in enterprise AI security:

1. **SHA-256 Hash vs Digital Signature** – How do we know downloaded model weights have not changed?
2. **Model Scanning and Backdoor Detection** – How can security teams detect suspicious model behavior?
3. **Complete Implementation** – Build an automated enterprise model security and approval pipeline.

**My recommendation:** Understand SHA-256 Hash vs Digital Signature first. This is the foundation of verifying model integrity before downloading and deploying models in an enterprise environment.
