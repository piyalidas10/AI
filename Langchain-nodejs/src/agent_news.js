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
    Search today's AI news.

    Return only the top five headlines with a one-line summary.
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
Here are today's top AI news headlines:

1.  **The AI industry is picking sides on open or closed tech. Experts say follow the money. - NBC News**
    The AI industry is divided on open vs. closed tech, with experts suggesting business interests drive these positions, as seen with Nvidia's open-source AI alliance and the absence of major closed-weight AI developers like OpenAI.

2.  **FactSet Announces Appointment of Chief People & Workforce Transformation Officer - AiThority**
    FactSet, a data and AI solutions provider, appointed Di Hirji as Chief People & Workforce Transformation Officer, emphasizing that becoming an AI-native company is as much about people and skills as it is about technology.

3.  **NCTC Aims To Create ‘Easy Button For AI’ - TV News Check**
    The National Content & Technology Cooperative (NCTC) is preparing to commercialize a subscription-based AI platform for its 700+ broadband operator members, aiming to simplify AI adoption.
--------------------------------
 */