# Langchain
Modern LangChain is built around Runnables (LCEL), and Chains and Agents are two major application patterns built on top of them.

LangChain Architecture
```
                    LangChain
                        │
        ┌───────────────┴───────────────┐
        │                               │
     Chains                         Agents
        │                               │
   Fixed Workflow               Dynamic Workflow
        │                               │
        └───────────────┬───────────────┘
                        │
                  Runnables (LCEL)
```

## Tutorials
1. Langchain: https://www.langchain.com/
2. JS Langchain Docs: https://js.langchain.com/docs/introduction/
3. Python Langchain Docs: https://python.langchain.com/docs/introduction/
4. V3 Langchain API: https://v03.api.js.langchain.com/index.html
5. Langchain chat: https://chat.langchain.com/
6. TavilySearch: https://www.tavily.com/
7. LangChain Tutorial 2025 | Build LLM Apps, Chains & Agents Step-by-Step : https://www.youtube.com/watch?v=GLpitbsSJtw&list=PLzjZaW71kMwS2MrPcY22-oZxHjrpi6yEZ&index=7
8. LangChain Agents Tutorial 2025 | Build AI-Powered Live News Q&A Agent ⚡LangChain 2025 Step-by-Step : https://www.youtube.com/watch?v=Z3vgQnQ2f1g&list=PLzjZaW71kMwS2MrPcY22-oZxHjrpi6yEZ&index=8
9. LangChain Agents Tutorial 2025 | Build AI-Powered Live News Q&A Agent ⚡LangChain 2025 Step-by-Step : https://www.youtube.com/watch?v=Z3vgQnQ2f1g&list=PLzjZaW71kMwS2MrPcY22-oZxHjrpi6yEZ&index=8
10. Build a Smart Restaurant AI Assistant ⚡ LangChain Agents + Gemini 2025 : https://www.youtube.com/watch?v=nVhl7NyTPXc&list=PLzjZaW71kMwS2MrPcY22-oZxHjrpi6yEZ&index=9

## Run files
```
node src/index.js
node src/chain.js
.
.
.
.
```

## what is HumanMessage?
HumanMessage is one of LangChain's message classes that represents a message sent by the user to a chat model.

LangChain models conversations as a sequence of messages rather than plain strings.

**Message Types :**

| Message Class   | Role                | Example                                         |
| --------------- | ------------------- | ----------------------------------------------- |
| `HumanMessage`  | User                | "What is AI?"                                   |
| `AIMessage`     | Assistant           | "AI is the simulation of human intelligence..." |
| `SystemMessage` | System instructions | "You are an expert JavaScript developer."       |
| `ToolMessage`   | Tool output         | Database/API search results                     |

**Example**
```
import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { HumanMessage } from "@langchain/core/messages";

const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  apiKey: process.env.GOOGLE_API_KEY,
});

const response = await model.invoke([
  new HumanMessage("Explain LangChain in simple terms.")
]);

console.log(response.content);
```
Output:
```
LangChain is a framework that helps developers build applications using Large Language Models...
```

### Why use HumanMessage instead of a string?

Both of these are valid.

**Option 1 (Simple String)**
```
const response = await model.invoke("What is AI?");
```
LangChain automatically converts the string into a HumanMessage.

**Option 2 (Explicit Message)**
```
const response = await model.invoke([
  new HumanMessage("What is AI?")
]);
```
This gives you more flexibility, especially for multi-turn conversations.

## Multi-turn Chat Example
```
import {
  HumanMessage,
  AIMessage,
  SystemMessage
} from "@langchain/core/messages";

const response = await model.invoke([
  new SystemMessage("You are a senior JavaScript teacher."),

  new HumanMessage("What is a Promise?"),

  new AIMessage(
    "A Promise represents the eventual completion of an asynchronous operation."
  ),

  new HumanMessage("Can you give me an example?")
]);

console.log(response.content);
```
Here the model receives the entire conversation history.

## When should you use PromptTemplate vs HumanMessage?

**Use PromptTemplate for parameterised prompts**
```
const prompt = PromptTemplate.fromTemplate(
  "Translate the following to French: {text}"
);

const chain = prompt.pipe(model);

await chain.invoke({
  text: "Hello"
});
```
Best for:
- LCEL chains
- RAG
- Agents
- Dynamic prompts


**Use HumanMessage for chat conversations**
```
await model.invoke([
  new HumanMessage("Tell me a joke.")
]);
```
Best for:
- Chatbots
- Conversation history
- Memory
- Multi-turn interactions