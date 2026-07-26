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
  new SystemMessage("You are a senior JavaScript teacher."),

  new HumanMessage("What is a Promise?"),

  new AIMessage(
    "A Promise represents the eventual completion of an asynchronous operation."
  ),

  new HumanMessage("Can you give me an example?")
]);


// The response is an AIMessage object that contains the model's reply.
// You can access the content of the message using the `content` property.
console.log(response.content);