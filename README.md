# AI
AI Terms You Need to Know: Agents, RAG, ASI &amp; More
```
Data → ML → DL → Transformers → LLMs
                     ↓
            GenAI + RAG + Agents
                     ↓
              Real Applications
```

<details>
<summary><strong>AI Youtube Videos</strong></summary>
[![20 AI Concepts Explained in 40 Minutes]](https://www.youtube.com/watch?v=OYvlznJ4IZQ)  
[![RAG Explained For Beginners]](https://www.youtube.com/watch?v=_HQ2H_0Ayy0)  

</details>

<details>
<summary><strong>What is AI ? How many types of AI ?</strong></summary>
AI is a computer program that can do things that normally require a human mind. This includes things like learning, recognizing patterns, understanding language, and making decisions.

This is the classic way to think about AI's "level of intelligence."

1️⃣ Types of AI based on Capability
----------------------------------------------------------------------------
**🔹 1. Narrow AI (Weak AI)**  
👉 Built to do one specific task really well.

Examples
  -  Chatbots likes ChatGPT
  -  Voice Assistants: Siri, Alexa, Google Assistant understanding your speech.
  -  Face recognition : Facebook recognizing faces in your photos.
  -  Recommendation systems (Netflix, Amazon): Netflix suggesting shows, Spotify creating Discover Weekly.
  -  Voice assistants (Alexa, Siri)
  -  Spam Filters: Your email client learning to detect junk mail.
  -  Navigation: Google Maps predicting traffic and optimizing your route.

**🔹 2. General AI (Strong AI)**   
👉 Can understand, learn, and apply knowledge across any intellectual task a human can.

Abilities
  -  Understand context
  -  Transfer knowledge between tasks
  -  Learn autonomously
  -  Theoretical Example: A robot that can cook breakfast, have a philosophical conversation, then learn to fix a car—all with common sense.

> 🚫 Does not exist yet (still theoretical)

**🔹 3. Super AI**  
👉 Intelligence that surpasses humans in every aspect. Self-improving, potentially incomprehensible to humans.

Examples (fictional)
  -  Skynet
  -  Jarvis (Iron Man)
  -  ⚠️ Purely hypothetical & sci-fi for now
  -  Theoretical Example: An AI that solves climate change, cures all diseases, and invents physics beyond our understanding.

2️⃣ Types of AI based on Functionality
----------------------------------------------------------------------------
**🔹 1. Reactive Machines**  
👉 No memory, no learning from past  
Example : IBM's Deep Blue (chess computer), basic spam filters.

**🔹 2. Limited Memory AI**  
👉 Uses past data to make decisions  
Examples : Self-driving cars, Chatbots, Recommendation engines  
✅ Most modern AI falls here

**🔹 3. Theory of Mind AI**  
👉 Understands emotions, beliefs, intentions  
🧠 Still in research phase

**🔹 4. Self-Aware AI**  
👉 Conscious, self-reflective  
🚫 Doesn’t exist. This would be a form of AGI/ASI.  
Example: A robot that knows it's a robot and has desires.

3️⃣ Types of AI based on Technology / Approach
----------------------------------------------------------------------------
**🔹 1. Machine Learning (ML) - AI that learns from data.**  
  -  Supervised Learning: Learns from labeled data (cat/not cat photos)
  -  Unsupervised Learning: Finds patterns in unlabeled data (customer segmentation)
  -  Reinforcement Learning: Learns by trial and error with rewards (AlphaGo)
  -  Semi-supervised Learning: Mix of labeled and unlabeled data

**🔹 2. Deep Learning (DL) - ML using neural networks**
  -  Image recognition
  -  Speech recognition
  -  LLMs
  -  Convolutional Neural Networks (CNNs): For images/video
  -  Recurrent Neural Networks (RNNs): For sequential data (time series, text)
  -  Transformers: The architecture behind ChatGPT (processes all data at once)
  -  Generative Adversarial Networks (GANs): Generate realistic fake data

**🔹 3. Natural Language Processing (NLP) - Understands human language**
  -  Translation
  -  Chatbots
  -  Sentiment analysis

**🔹 4. Computer Vision - Interprets images & videos**
  -  Face detection
  -  OCR
  -  Medical imaging

**🔹 5. Generative AI 🔥 - Creates new content**
  -  Text (ChatGPT)
  -  Images (DALL·E)
  -  Code (Copilot)

**🔹 6. Robotics: AI in physical machines** 
  -  Boston Dynamics robots

**🔹 7. Discriminative AI - Classifies or distinguishes between things**  
  -  Spam filters
  -  facial recognition
  -  medical diagnosis AI

**🔹 8. Predictive AI - Forecasts future outcomes**
  -  Stock prediction
  -  weather forecasting
  -  demand planning

</details>

<details>
<summary><strong>Imagine you're using a Financial Research Agent. You ask: "Analyze Tesla's Q4 2024 prospects and recommend if we should invest.". Let’s walk through exactly what happens</strong></summary>

> “A financial research agent decomposes the investment query, retrieves real-time market data via tools, performs financial and qualitative reasoning, evaluates risks through scenarios, applies compliance guardrails, and generates a probabilistic recommendation.”

🟢 STEP 1: Query Understanding (Intent Parsing)
----------------------------------------------------------------------------------
The agent first understands what you want, not just the words.  
It extracts:
  -  Company → Tesla (TSLA)
  -  Timeframe → Q4 2024
  -  Task → Analysis + Recommendation
  -  Domain → Financial / Investment
  -  Decision Type → Buy / Hold / Sell
  -  Risk → High-stakes financial advice ⚠️

📌 Internally:
```
Intent: Investment decision
Assets involved: Public equity
Constraints: Needs up-to-date financial data
```

🟢 STEP 2: Task Decomposition (Agent Planning)
----------------------------------------------------------------------------------
The agent breaks the problem into subtasks.  
Typical plan:
  -  Collect Tesla Q4 2024 data
  -  Analyze financial performance
  -  Analyze business & market factors
  -  Analyze risks
  -  Compare with peers
  -  Generate investment recommendation
  -  Add disclaimer & confidence level

📌 This is called agent planning.

🟢 STEP 3: Data Collection (Tool Use 🔧)
----------------------------------------------------------------------------------
The agent now calls tools, not its memory.  
Data Sources:
  -  Earnings reports (Q4 2024)
  -  Revenue, margins, EPS
  -  Vehicle delivery numbers
  -  Energy business performance
  -  Market news (price cuts, competition)
  -  Macroeconomic data (interest rates)
  -  Analyst consensus

📌 Internally:
```
Tool: Financial API
Tool: Market News API
Tool: SEC filings
```
**👉 This is where RAG (Retrieval-Augmented Generation) happens.**

🟢 STEP 4: Data Validation & Freshness Check
----------------------------------------------------------------------------------
The agent checks:
  -  Is the data latest?
  -  Any conflicting numbers?
  -  Missing info?

If something is outdated:
  -  ➡️ It re-queries sources
  -  ➡️ Or marks uncertainty explicitly

🟢 STEP 5: Financial Analysis
----------------------------------------------------------------------------------
Now the reasoning kicks in.  
The agent analyzes:
  -  Revenue growth / decline
  -  Gross margin trends
  -  EPS vs expectations
  -  Cash flow
  -  CapEx & R&D
  -  Price-cut impact on margins

> 📌 Example reasoning: “Margins declined due to aggressive pricing, but delivery volume grew.”

🟢 STEP 6: Business & Strategic Analysis
----------------------------------------------------------------------------------
The agent evaluates qualitative factors:
  -  EV market competition (BYD, legacy auto)
  -  FSD progress & regulation
  -  Energy storage growth
  -  AI / robotics optionality
  -  CEO influence (Elon factor)
  -  This is non-numeric reasoning.

🟢 STEP 7: Risk Assessment ⚠️
----------------------------------------------------------------------------------
Critical step for financial agents.  
Risks Identified:
  -  Margin compression
  -  Regulatory scrutiny
  -  Demand volatility
  -  China market risk
  -  Interest rate sensitivity
  -  Each risk is weighted.

🟢 STEP 8: Scenario Modeling
----------------------------------------------------------------------------------
The agent often simulates multiple futures:  
| Scenario  | Outcome                   |
| --------- | ------------------------- |
| Bull Case | Strong AI + Energy growth |
| Base Case | Stable but slow growth    |
| Bear Case | Margin erosion continues  |

🟢 STEP 9: Recommendation Logic
----------------------------------------------------------------------------------
Now comes the decision engine.  

The agent:
  -  Matches analysis to investor profile
  -  Applies investment heuristics
  -  Considers valuation vs growth

📌 Example logic:
```
If risk > reward → HOLD
If upside >> downside → BUY
```

🟢 STEP 10: Safety & Compliance Layer 🛡️
----------------------------------------------------------------------------------
Because this is financial advice, the agent:
  -  Avoids guarantees
  -  Uses probabilistic language
  -  Adds disclaimers
  -  Encourages independent judgment
  -  This is Responsible AI enforcement.

🟢 STEP 11: Response Generation
----------------------------------------------------------------------------------
Finally, the agent writes the answer:

Typical structure:
  -  Executive summary
  -  Financial performance
  -  Growth drivers
  -  Risks
  -  Final recommendation
  -  Confidence level

🟢 STEP 12: Output to User 📤
----------------------------------------------------------------------------------
You receive a clear, structured, decision-oriented answer like:
```
Recommendation: HOLD (Moderate Risk)
Tesla shows innovation strength, but near-term margin pressure limits upside in Q4 2024.
```

</details>

