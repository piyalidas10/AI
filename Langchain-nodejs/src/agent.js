import { config } from "dotenv";
config();

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { TavilySearch } from "@langchain/tavily";

// 1. Create the model
const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  temperature: 0.7,
  maxOutputTokens: 2048,
  apiKey: process.env.GOOGLE_API_KEY,
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
 */
const searchTool = new TavilySearch({
  apiKey: process.env.TAVILY_API_KEY,
  maxResults: 5,
  topic: "general", // "general" or "news"
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
const agent = createReactAgent({
  llm: model,
  tools: [searchTool],
});

/**
 * agent.invoke() is a method that allows you to interact with the React Agent by sending user messages and receiving responses based on the integrated tools and model.
 * 
 * The method takes an object with a "messages" property, which is an array of message objects. 
 * Each message object should have a "role" (e.g., "user") and "content" (the actual message text).
 */
const result = await agent.invoke({
  messages: [
    {
      role: "user",
      content: "What is the latest news about ISRO?"
    }
  ]
});

console.log(result);