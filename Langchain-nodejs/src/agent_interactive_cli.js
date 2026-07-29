import "dotenv/config";
import readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { TavilySearch } from "@langchain/tavily";
import { createReactAgent } from "@langchain/langgraph/prebuilt";

const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  apiKey: process.env.GOOGLE_API_KEY,
});

// tavily search tool
// The TavilySearch tool allows the agent to perform web searches and retrieve relevant information from the internet.
// It is configured with an API key and a maximum number of results to return.
const tools = [
  new TavilySearch({
    apiKey: process.env.TAVILY_API_KEY,
    maxResults: 5,
  }),
];

// ReAct Agent
// The ReAct agent is created using the Gemini LLM and the Tavily Search tool.
// It can process user queries, perform web searches, and provide relevant information in response to user prompts.
const agent = createReactAgent({
  llm: model,
  tools,
});

// readline interface for interactive CLI
// The readline interface allows the user to interact with the agent through the command line.
// input: stdin and output: stdout are used to read user input and display the agent's responses.
const rl = readline.createInterface({
  input: stdin,
  output: stdout,
});

console.log("🤖 Gemini Research Agent");
console.log("Type 'exit' to quit.\n");

while (true) {
  const question = await rl.question("You > ");

  if (question.toLowerCase() === "exit") break;

  // Invoke the agent with a user query
    /**
     * The agent is invoked with a user query asking for the current CEO of OpenAI.
     * The agent will perform a web search if necessary and provide a concise answer.
     * role: "user" indicates that the message is from the user, and the content contains the query.
     * role: "assistant" indicates that the message is from the assistant, and the content contains the response.
     * role: "system" indicates that the message is from the system, and the content contains instructions or context for the agent.
     * role: "tool" indicates that the message is from a tool, and the content contains information retrieved from a tool.
     * role: "function" indicates that the message is from a function, and the content contains information returned from a function call.
     * role: "error" indicates that the message is from an error, and the content contains information about an error that occurred during processing.
     * 
     * how many roles are there in the messages array? 
     * There are 6 roles in the messages array: "user", "assistant", "system", "tool", "function", and "error".
     * 
     * what is the purpose of the messages array? 
     * The messages array is used to provide context and instructions to the agent, allowing it to understand the user's query and generate an appropriate response.
     */
  const result = await agent.invoke({
    messages: [
      {
        role: "user",
        content: question,
      },
    ],
  });

  console.log("\nAssistant:\n");
  console.log(result.messages.at(-1).content);
  console.log("\n--------------------------------------\n");
}

rl.close();

/**
 * 🤖 Gemini Research Agent
Type 'exit' to quit.

You > Who won the FIFA World Cup in 2022?

Assistant:

Argentina won the 2022 FIFA World Cup, defeating France in the final after a penalty shootout. Lionel Messi was awarded the Golden Ball.

--------------------------------------

You > What are the latest Angular features?

Assistant:

(Uses Tavily to search the web and summarizes the latest Angular updates.)

--------------------------------------

You > exit
 */