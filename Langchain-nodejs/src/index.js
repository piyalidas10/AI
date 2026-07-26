import "dotenv/config";

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { HumanMessage } from "@langchain/core/messages";

const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  temperature: 0.7,
  apiKey: process.env.GOOGLE_API_KEY,
});

/**
 * HumanMessage is one of LangChain's message classes that represents a message sent by the user to a chat model.
 * LangChain models conversations as a sequence of messages rather than plain strings.
 * 
 * Message Types
 * | Message Class   | Role                | Example                                         |
 * | --------------- | ------------------- | ----------------------------------------------- |
 * | `HumanMessage`  | User                | "What is AI?"                                   |
 * | `AIMessage`     | Assistant           | "AI is the simulation of human intelligence..." |
 * | `SystemMessage` | System instructions | "You are an expert JavaScript developer."       |
 * | `ToolMessage`   | Tool output         | Database/API search results                     |
 */
const response = await model.invoke([
  new HumanMessage("Explain LangChain in simple words.")
]);

// The response is an AIMessage object that contains the model's reply.
// You can access the content of the message using the `content` property.
console.log(response.content);

/**
 ***********************************Answers*************************************************
 * 
 * Imagine you have a super-smart, incredibly knowledgeable friend (that's your **Large Language Model, or LLM**, like ChatGPT).

This friend is amazing at answering questions, writing stories, and summarizing information. But this friend has a few quirks:

1.  **No Memory:** They forget everything you said in the previous sentence.
2.  **No Tools:** They can't look things up on the internet, do math calculations, or interact with other software. They only know what they were trained on.
3.  **Gets Confused by Big Tasks:** If you ask them to "Plan my trip to Paris, including flights, hotels, and local attractions," they might struggle to break it down and do it step-by-step.

**LangChain is like a personal assistant or a project manager for your super-smart LLM friend.**

Here's what LangChain helps your LLM do:

*   **Memory:** It gives your LLM a "memory" so it can remember previous parts of your conversation and maintain context.
*   **Tools:** It gives your LLM "tools" – like handing it a calculator, a web browser, a calendar, or access to a database. So, the LLM can decide, "Hmm, I need to look up current flight prices, so I'll use the web search tool."
*   **Chains (Steps):** It helps your LLM break down complex problems into smaller, manageable steps, and then execute those steps in order. For example, "First, find flights. Second, find hotels. Third, suggest attractions."
*   **Connect to Different LLMs:** It lets you easily swap out different LLMs (e.g., use Google's LLM for one part of the task, and OpenAI's for another).

**In simple words:**

LangChain is a **toolkit or framework** that helps you build **smarter, more capable, and context-aware applications** using Large Language Models, by giving them memory, tools, and the ability to handle multi-step tasks.

It takes a powerful but basic LLM and turns it into something that can truly act like an intelligent, interactive agent.
 */