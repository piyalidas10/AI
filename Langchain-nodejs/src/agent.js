import { config } from "dotenv";
config();

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { TavilySearch } from "@langchain/tavily";
import { HumanMessage } from "@langchain/core/messages";
import { createReactAgent } from "@langchain/langgraph/prebuilt";

// =======================================================
// Validate Environment Variables
// =======================================================

if (!process.env.GOOGLE_API_KEY) {
  throw new Error("GOOGLE_API_KEY is missing.");
}

if (!process.env.TAVILY_API_KEY) {
  throw new Error("TAVILY_API_KEY is missing.");
}

// =======================================================
// Gemini Model
// =======================================================

// 1. Create the model
// The SDK automatically reads: GOOGLE_API_KEY from .env.
const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  temperature: 0.7,
  maxOutputTokens: 2048,
});

/**
 * This is an example of how to create a React Agent using the LangChain library. 
 * The agent is configured with a Google Generative AI model and a Tavily search tool. 
 * The agent can be invoked with user messages to get responses based on the provided tools and model.
 * 
 * The example demonstrates the following steps:
 * 1. Import necessary modules and configure environment variables.
 * 2. Create a Google Generative AI model with specified parameters.
 * 3. Create a Tavily search tool with an API key and configuration.
 * 4. Create a React Agent using the model and tools.
 * 5. Invoke the agent with user messages and log the result.
 * 
 * Note: Ensure that you have the required API keys set in your environment variables for both Google Generative AI and Tavily search tool.
 * 
 * topic: "general" or "news" - This parameter specifies the type of content to be searched by the Tavily search tool.
 * general: Searches the web broadly. The agent can be used to answer questions, provide information, or perform tasks based on the capabilities of the integrated tools and model.
 * news: Focuses on recent and news-oriented content. The agent can be used to fetch the latest news articles or updates based on user queries.
 * 
 * The Tavily package also automatically reads: TAVILY_API_KEY  from .env.
 */
// =======================================================
// Tavily Search Tool
// =======================================================
const tavily = new TavilySearch({
  maxResults: 5,
  topic: "general",
});

/**
 * This is an example of how to create a React Agent using the LangChain library.
 * The agent is configured with a Google Generative AI model and a Tavily search tool.
 * The agent can be invoked with user messages to get responses based on the provided tools and model.
 * 
 * The example demonstrates the following steps:
 * 1. Import necessary modules and configure environment variables.
 * 2. Create a Google Generative AI model with specified parameters.
 */
// =======================================================
// Create React Agent
// =======================================================
const agent = createReactAgent({
  model,
  tools: [tavily],
});

/**
 * agent.invoke() is a method that allows you to interact with the React Agent by sending user messages and receiving responses based on the integrated tools and model.
 * 
 * The method takes an object with a "messages" property, which is an array of message objects. 
 * Each message object should have a "role" (e.g., "user") and "content" (the actual message text).
 * 
 * If you do: console.log(response);
 * The object may contain:
    {
      messages: [
        HumanMessage {},
        AIMessage {}
      ]
    }
  
  Using: console.log(JSON.stringify(response, null, 2)); formats the object into readable JSON (when the object is serializable).
  A better way to inspect them is: console.dir(response, { depth: null });
 */
// =======================================================
// Execute
// =======================================================
try {

  const result = await agent.invoke({
    messages: [
      new HumanMessage(
        "What is the latest news about ISRO?"
      ),
    ],
  });

  console.dir(result, {
    depth: null,
    colors: true,
  });

  console.log("\n==============================");

  console.log(result.messages.at(-1)?.content);

} catch (err) {

  console.error("\nAgent Error\n");

  console.error(err);

}