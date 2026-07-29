import "dotenv/config";

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { TavilySearch } from "@langchain/tavily";
import { createReactAgent } from "@langchain/langgraph/prebuilt";

const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  temperature: 0.2,
  apiKey: process.env.GOOGLE_API_KEY,
});

// Tavily Search Tool
// The TavilySearch tool allows the agent to perform web searches and retrieve relevant information from the internet.
// It is configured with an API key and a maximum number of results to return.
const searchTool = new TavilySearch({
  apiKey: process.env.TAVILY_API_KEY,
  maxResults: 3,
});

// ReAct Agent
// The ReAct agent is created using the Gemini LLM and the Tavily Search tool.
// It can process user queries, perform web searches, and provide relevant information in response to user prompts.
const agent = createReactAgent({
  llm: model,
  tools: [searchTool],
});

async function research(topic) {
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
     * 
     * agent.stream() is used to stream the response from the agent in real-time, allowing for a more interactive experience. 
     * The streamMode: "values" option specifies that the stream should return individual message chunks as they are generated.
     */
  const stream = await agent.stream(
    {
      messages: [
        {
          role: "user",
          content: `
        Research the following topic:

        ${topic}

        Requirements:
        - Search the web if required.
        - Summarize the findings.
        - Mention important facts.
        - Mention latest updates.
        - Give references.
        `,
                },
            ],
            },
            {
            streamMode: "values",
            }
        );

  for await (const chunk of stream) {
    const message = chunk.messages.at(-1);

    if (message?.content) {
      console.log("--------------------------------");
      console.log(message.content);
      console.log("--------------------------------\n");
    }
  }
}

research("Latest Angular 20 features");

/**
 * {
    "query": "Angular 20 features",
    "follow_up_questions": null,
    "answer": null,
    "images": [],
    "results": [
        {
        "url": "https://www.kellton.com/kellton-tech-blog/angular-20-new-features-guide",
        "title": "Angular 20 New Features: Complete Developer Guide",
        "content": "Angular 20 is the May 2025 major release of Google's TypeScript-based frontend framework. It is not an incremental update — it marks the stabilization of Angular's new reactive architecture. Features that were in developer preview in Angular 18 and 19 — including the Signals API, incremental hydration, and modern control flow blocks — are now production-stable. [...] Angular 20 new features mark a fresh chapter for the framework, bringing in stronger reactivity, zoneless change detection, and more advanced SSR capabilities. These improvements unlock exciting possibilities for developers, but they also come with a set of real-world challenges. From adjusting to the Signals API to rethinking how apps handle hydration, the Angular 20 release requires teams to adapt. Let’s look at the most common hurdles and how you can tackle them with confidence. [...] Angular 20 is the latest version of Google’s TypeScript-based web development framework. It focuses on performance, developer experience, and modern reactivity with stable Signals API, zoneless change detection, incremental hydration, and modernized template syntax.\n\n### 2. What are the biggest new features in Angular 20?\n\nAngular 20 introduces stable signals, zoneless change detection, incremental hydration for SSR, and modern JavaScript-like template syntax.",
        "score": 0.93624437,
        "raw_content": null
        },
        {
        "url": "https://medium.com/@rohitjsingh16/angular-20-features-whats-new-in-2025-with-examples-204c7720c4f4",
        "title": "Medium",
        "content": "Whether you’re building small apps or enterprise-grade platforms, Angular 20 makes development faster, safer, and more future-ready.\n\n👉 Have you tried Angular 20 yet? What’s your favorite new feature? Let me know in the comments!\n\n--\n\n--\n\n🚀 Rohit Singh 🚀\n🚀 Rohit Singh 🚀\n\n## Written by 🚀 Rohit Singh 🚀\n\nHelping developers build scalable Angular & Node.js applications with practical tutorials, performance tips, and architecture insights.\n\nHelp\n\nStatus\n\nAbout\n\nCareers\n\nPress\n\nBlog\n\nStore\n\nPrivacy [...] If you’re wondering what’s new in Angular 20 and why you should upgrade, this guide will walk you through the top features, examples, and migration tips.\n\n## 🔥 1. Stable Angular Signals\n\nAngular Signals, introduced experimentally in Angular 16, have now reached full stability in Angular 20.\n\nExample — Counter App with Signals:\n\n👉 No need for `BehaviorSubject` or `NgRx` for simple cases. Signals make Angular apps more reactive and predictable.\n\n`BehaviorSubject`\n`NgRx` [...] Sign up\n\nSign in\n\nSign up\n\nSign in\n\nUnknown user\n\n# Ang🚀 Angular 20 Features & What’s New in 2025 (With Examples)\n\n🚀 Rohit Singh 🚀\n\n--\n\nListen\n\nShare\n\nAngular continues to evolve as one of the most popular front-end frameworks, and with Angular 20, the team has introduced powerful new features, performance upgrades, and developer experience improvements.",
        "score": 0.8700796,
        "raw_content": null
        },
        {
        "url": "https://blog.angular.dev/angular-summer-update-2025-1987592a0b42",
        "title": "Angular Summer Update 2025. Authors: Jens Kuehlers Mark Techson | by Angular | Angular Blog",
        "content": "Since launching Angular v20 in May, the team has been hard at work shipping new features and improvements in v20.1 and v20.2. We are continuing our mission to boost developer productivity and help you create apps your users will love. As part of that mission, we’ve also expanded our AI offerings to enhance your development workflow.\n\nHighlights [...] In v20, we landed angular.dev/ai, the destination for all things Angular & AI. We’ve created all-new guides on how to build AI-powered applications using technologies such as Genkit, Firebase AI Logic or by using the Gemini API. You can also find code samples, video guides and helpful best practices to make sure you can have the best experience when developing with AI tooling or AI powered applications. [...] Zones served as the mechanic that drove the Angular change detection cycle. While it had its benefits there issues surfaced over time including difficulty debugging apps, larger bundle sizes and more. As a result, developers have been asking for optional zones for some time and the team has been diligently working on making it a reality. We’re excited to announce that as of Angular v20.2, zoneless Angular is stable. That means you can use it in production. To get started, you’ll want to update",
        "score": 0.76554126,
        "raw_content": null
        }
    ],
    "response_time": 1.05,
    "request_id": "7690e6fa-4af4-4e1d-a6fe-37483f2a4bcb"
    }
 */