import "dotenv/config";

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { TavilySearch } from "@langchain/tavily";
import { createReactAgent } from "@langchain/langgraph/prebuilt";

const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  temperature: 0.2,
  apiKey: process.env.GOOGLE_API_KEY,
});

const searchTool = new TavilySearch({
  apiKey: process.env.TAVILY_API_KEY,
  maxResults: 3,
});

const agent = createReactAgent({
  llm: model,
  tools: [searchTool],
});

async function research() {
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
      content: `
    Research OpenAI.

    Find:

    - CEO
    - Employees
    - Latest funding
    - Major products
    - Recent announcements
    `,
        },
    ],
    });

        console.log("--------------------------------");
        console.log(result.messages.at(-1).content);
        console.log("--------------------------------\n");
}

research();

/**
 * --------------------------------
Here's the information about OpenAI:

*   **CEO:** Sam Altman
*   **Employees:** As of June 30, 2026, OpenAI has 10,050 employees.
*   **Latest funding:** OpenAI raised $6.6 billion in its latest funding round.
*   **Major products:** ChatGPT is a major product, and OpenAI operates in the Generative AI, AI Infrastructure, and Artificial Intelligence sectors.
*   **Recent announcements:** In February 2026, Sam Altman announced that ChatGPT is "back to exceeding 10% monthly growth" and that an "updated Chat model" was being prepared for launch that week.
--------------------------------
 */