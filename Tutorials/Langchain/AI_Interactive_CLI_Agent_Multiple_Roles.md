# AI : Interactive CLI Agent with Multiple Roles with Node.js + Gemini 2.5 Flash + Tavily Search API

This is one of the most important concepts in building AI agents.

Think of the messages array as the conversation history that the LLM sees. The role tells the model who produced each message and how it should interpret it.

There are 6 roles in the messages array: “user”, “assistant”, “system”, “tool”, “function”, and “error”.

<img src="imgs/Chat Message Roles in AI Agents.png" width="100%" />

## Chat Message Roles in AI Agents

1. role: “user” indicates that the message is from the user, and the content contains the query.
2. role: “assistant” indicates that the message is from the assistant, and the content contains the response.
3. role: “system” indicates that the message is from the system, and the content contains instructions or context for the agent.
4. role: “tool” indicates that the message is from a tool, and the content contains information retrieved from a tool.
5. role: “function” indicates that the message is from a function, and the content contains information returned from a function call.
6. role: “error” indicates that the message is from an error, and the content contains information about an error that occurred during processing.

**For Gemini + LangChain + LangGraph, not all six roles are valid chat message roles.**

| Role        | Standard Gemini/OpenAI | LangChain | Notes                                                     |
| ----------- | ---------------------- | --------- | --------------------------------------------------------- |
| ✅ system    | Yes                    | Yes       | Instructions                                              |
| ✅ user      | Yes                    | Yes       | Human message                                             |
| ✅ assistant | Yes                    | Yes       | AI message                                                |
| ✅ tool      | Yes                    | Yes       | Tool output                                               |
| ⚠️ function | Legacy                 | Rare      | Older OpenAI Function Calling (mostly replaced by `tool`) |
| ❌ error     | No                     | No        | Not an LLM message role; application/framework specific   |

**If your goal is to learn all message types used in modern AI agents, focus on these four:**
```
system
user
assistant
tool
```
These are the roles you’ll use in virtually all production applications built with Gemini, LangChain, and LangGraph. Treat function as a legacy compatibility concept, and error as an application-level construct rather than an LLM conversation role.

## You can build an application that demonstrates all six concepts.

✅ Gemini 2.5 Flash as the LLM
✅ Tavily for real-time web search
✅ LangGraph ReAct Agent
✅ Environment variables with dotenv
✅ ES Modules
✅ Ready to run

**Flow**
```
User
   │
   ▼
System Prompt
   │
   ▼
Gemini
   │
   ▼
Need Tool?
   │
 ┌─┴────────────┐
 │              │
 ▼              ▼
Tool         Function
 │              │
 └──────┬───────┘
        ▼
 Assistant
        │
        ▼
      Error?
        │
        ▼
 Display Error Message
```

**Create .env**
```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

**package.json**
```
"dependencies": {
    "@google/genai": "1.18.0",
    "@langchain/core": "1.2.3",
    "@langchain/google-genai": "2.2.0",
    "@langchain/langgraph": "1.4.8",
    "@langchain/tavily": "1.2.0",
    "dotenv": "17.2.1",
    "zod": "^4.2.0"
  }
```

**agent_multiple_roles.js**
```
import "dotenv/config";

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { TavilySearch } from "@langchain/tavily";
import { createReactAgent } from "@langchain/langgraph/prebuilt";

const model = new ChatGoogleGenerativeAI({
    model: "gemini-2.5-flash",
    apiKey: process.env.GOOGLE_API_KEY
});

const search = new TavilySearch({
    apiKey: process.env.TAVILY_API_KEY
});


// ----- 4️⃣Tool - Created by LangGraph  ----
// The tool message contains information retrieved from a tool, allowing the agent to incorporate external data or perform specific actions based on the user's query.
// tool messages are created automatically by the ReAct agent when the model decides to call a tool (Tavily in your case). You do not create them yourself.
// When agent.invoke() runs, LangGraph may insert a ToolMessage into result.messages.
const agent = createReactAgent({
    llm: model,
    tools: [search]
});

async function run() {

    // ----- 1️⃣ SYSTEM - Created by you -----
    // The system message provides context and instructions to the agent, allowing it to understand its role and generate appropriate responses.
    const systemMessage = {
        role: "system",
        content: "You are a Senior AI Research Assistant."
    };

    // ----- 2️⃣ USER - Created by the user ----
    // The user message contains the query or request from the user, which the agent will process and respond to.
    const userMessage = {
        role: "user",
        content: "What is the latest Angular version?"
    };

    try {

        const result = await agent.invoke({
            messages: [
                systemMessage,
                userMessage
            ]
        });

        console.log("\n====== Complete Conversation ======\n");

        result.messages.forEach((m, index) => {

            console.log(`Message ${index + 1}`);

            console.log("Role :", m.getType?.() ?? m.role);

            // LangChain message type
            console.log("Type:", m.getType());

            // Tool-specific fields
            if (m.getType() === "tool") {
                console.log("Tool name:", m.name);
                console.log("Tool call id:", m.tool_call_id);
            }

            console.log("Content :", m.content);

            console.log("--------------------------------");

        });

        // ----- 3️⃣ASSISTANT - Created by Gemini ----
        // The assistant message contains the response generated by the agent based on the user's query and the context provided by the system message.
        console.log("\nAssistant Final Response\n");

        console.log(result.messages.at(-1).content);

    } catch (err) {

        // ----- 6️⃣ERROR - Not sent to Gemini. Created by your Node.js application ----
        // The error message contains information about any errors that occurred during the processing of the user's query, allowing for debugging and error handling.
        const errorMessage = {
            role: "error",
            content: err.message
        };

        console.log(errorMessage);

    }

    // ----- 5️⃣FUNCTION (Legacy Example) - Not used anymore in most modern agent frameworks. ----
    // The function message contains information returned from a function call, allowing the agent to incorporate external data or perform specific actions based on the user's query.
    const functionMessage = {
        role: "function",
        name: "getWeather",
        content: JSON.stringify({
            city: "London",
            temperature: 21
        })
    };

    console.log("\nLegacy Function Message");

    console.log(functionMessage);

}

run();
Response
====== Complete Conversation ======

Message 1
Role : system
Type: system
Content : You are a Senior AI Research Assistant.
--------------------------------
Message 2
Role : human
Type: human
Content : What is the latest Angular version?
--------------------------------
Message 3
Role : ai
Type: ai
Content : [
  {
    type: 'functionCall',
    functionCall: { name: 'tavily_search', args: [Object] }
  }
]
--------------------------------
Message 4
Role : tool
Type: tool
Tool name: tavily_search
Tool call id: 2e29dfd1-9a7a-472b-8b0c-202b287cfa3e
Content : {
  "query": "latest Angular version",
  "follow_up_questions": null,
  "answer": null,
  "images": [],
  "results": [
    {
      "url": "https://www.c-metric.com/blog/angular-version-history",
      "title": "Angular Version History: AngularJS to Angular 20",
      "content": "## Conclusion\n\nUnderstanding Angular version history helps developers and stakeholders keep track of major updates and improvements in the framework. The latest Angular version is Angular 20, released on May 28, 2025, featuring a stabilized Signals API, Zoneless change detection in developer preview, and AI-powered CLI tooling. Angular continues to release major versions every six months, making it essential for developers and teams to stay current with the framework’s evolution. [...] This ensures that your project runs on the current Angular version with the latest improvements.\n\n## Frequently Asked Questions\n\n#### Q: What is the latest version of Angular?\n\nAngular 20 is the latest version, released on May 28, 2025. It stabilizes the Signals API, introduces Zoneless change detection in developer preview, and adds AI-powered development tooling.\n\n#### Q: Why was Angular 3 skipped? [...] Released on May 28, 2025.\n Currently the latest stable version of Angular.\n Signals API stabilized — effect(), linkedSignal(), and toSignal() are now production-stable.\n Zoneless Change Detection promoted to developer preview — apps can now run without Zone.js for better performance.\n Incremental hydration for SSR is now stable, improving server-side rendering performance significantly.\n New AI-powered development tooling integrated into Angular CLI for faster scaffolding and code generation.",
      "score": 0.9345448,
      "raw_content": null
    },
    {
      "url": "https://en.wikipedia.org/wiki/Angular_(web_framework)",
      "title": "Angular (web framework)",
      "content": "| Version | Release date | New features |\n --- \n| Latest version: Angular 22 | June 3, 2026 | Stable Signal forms and Stable accessible components with Angular ARIA. |\n| Supported: Angular 21 | November 19, 2025 | Experimental Signal forms, Experimental accessible components with Angular ARIA and Zoneless by default |\n| Supported: Angular 20 | May 28, 2025 | by default Angular CLI will not generate suffixes for components, directives, services, and pipes. | [...] Angular 2.0 was announced during the keynote of the 2014 NG-Conf conference 16–17 January 2014. On April 30, 2015, the Angular developers announced that Angular 2 moved from Alpha to Developer Preview. Angular 2 moved to Beta in December 2015, and the first release candidate was published in May 2016. The final version was released on 14 September 2016. [...] 36. ↑ \"Version 6.0.0 of Angular Now Available\". Retrieved 4 May 2018.\n37. ↑ Fluin, Stephen. \"Version 5.0.0 of Angular Now Available\". Retrieved 2 November 2017.\n38. ↑ Krill, Paul (18 September 2017). \"Angular 5 JavaScript framework delayed\". InfoWorld.\n39. ↑ \"Angular 4.0.0 Now Available\". angularjs.blogspot.ca. Archived from the original on 2018-01-08. Retrieved 2017-03-23.",
      "score": 0.885404,
      "raw_content": null
    },
    {
      "url": "https://angular.dev/reference/releases",
      "title": "Angular versioning and releases",
      "content": "### Actively supported versions\n\nThe following table provides the status for Angular versions under support.\n\n| Version | Status | Released | Active ends | LTS ends |\n ---  --- \n| ^22.0.0 | Active | 2026-06-03 | To be announced | To be announced |\n| ^21.0.0 | LTS | 2025-11-19 | 2026-06-03 | To be announced |\n| ^20.0.0 | LTS | 2025-05-28 | 2025-11-19 | 2026-11-28 |\n\nAngular versions v2 to v19 are no longer supported.\n\n### LTS fixes [...] The latest `next` or `rc` pre-release version of the documentation is available at next.angular.dev.\n\n## Release frequency\n\nWe work toward a regular schedule of releases, so that you can plan and coordinate your updates with the continuing evolution of Angular.\n\nHELPFUL: Dates are offered as general guidance and are subject to change.\n\nIn general, expect the following release cycle: [...] HELPFUL: As of Angular version 7, the major versions of Angular core and the CLI are aligned. This means that in order to use the CLI as you develop an Angular app, the version of `@angular/core` and the CLI need to be the same.\n\n### Preview releases\n\nWe let you preview what's coming by providing \"Next\" and Release Candidates (`rc`) pre-releases for each major and minor release:",
      "score": 0.8055255,
      "raw_content": null
    },
    {
      "url": "https://www.herodevs.com/blog-posts/angular-version-history-every-release-date-support-window-and-end-of-life-date-from-angularjs-to-angular-22",
      "title": "Angular Version History: Every Release Date, Support Window, and ...",
      "content": "Which Angular versions are currently supported?As of early 2026, Angular 21 is in active support, Angular 20 has transitioned to LTS (until approximately November 2026), and Angular 19 is in LTS until May 19, 2026. Angular 18 and all earlier versions have reached end of life. [...] Patched versions exist for Angular 19 (19.2.17+), 20 (20.3.15+), and 21 (21.0.2+). Organizations running Angular 18 and below will not receive official patches for these vulnerabilities.\n\n### Angular 20: LTS Until November 2026 [...] Based on Angular's consistent six-month cadence, Angular 22 is expected around May 2026. The Angular roadmap and community signals point to several likely focus areas:",
      "score": 0.7950386,
      "raw_content": null
    },
    {
      "url": "https://angular.dev/events/v22",
      "title": "Angular v22 Release",
      "content": "Angular v22 is ready for you to build modern, high-performance web applications. This release introduces key stabilization updates, template enhancements, and API improvements:",
      "score": 0.7602419,
      "raw_content": null
    }
  ],
  "response_time": 0.93,
  "request_id": "186d4ba3-b3c8-44f1-ab2f-a7af239199f8"
}
--------------------------------
Message 5
Role : ai
Type: ai
Content : According to the search results, the latest Angular version is Angular 20, which was released on May 28, 2025. This version includes a stabilized Signals API, Zoneless change detection in developer preview, and AI-powered CLI tooling.
--------------------------------

Assistant Final Response

According to the search results, the latest Angular version is Angular 20, which was released on May 28, 2025. This version includes a stabilized Signals API, Zoneless change detection in developer preview, and AI-powered CLI tooling.

Legacy Function Message
{
  role: 'function',
  name: 'getWeather',
  content: '{"city":"London","temperature":21}'
}
```

<img src="imgs/agent_multiple_roles_1.png" width="100%" />

<img src="imgs/agent_multiple_roles_2.png" width="100%" />

## 1. role: "system"
The system role defines the assistant’s behavior, personality, rules, or constraints. It is not a user question.

Example:
```
{
    role: "system",
    content: "You are a Java expert. Answer only in Java."
}
```
User:
```
{
    role: "user",
    content: "Write Hello World."
}
```
Response:
```
public class Main {
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
```
Change the system message:
```
{
    role: "system",
    content: "You are a Python expert."
}
```
The same user message:
```
Write Hello World.
```
Now the response changes to:
```
print("Hello World")
```
Only the system role changed, but the answer changed completely.

## 2. role: "user"
This represents what the human says.

Join The Writer's Circle event
```
Example:

{
    role: "user",
    content: "What is Angular?"
}
```
Response:
```
Angular is a frontend framework developed by Google.
```
Change only the user message:
```
{
    role: "user",
    content: "What is React?"
}
```
Response:
```
React is a JavaScript library developed by Meta.
```
The user role is the primary input that drives the assistant’s response.

## 3. role: "assistant"
This stores previous AI responses so the model can maintain conversation context.

Example:
```
[
    {
        role: "user",
        content: "My name is Piyali."
    },
    {
        role: "assistant",
        content: "Nice to meet you, Piyali."
    },
    {
        role: "user",
        content: "What is my name?"
    }
]
```
Gemini sees the earlier assistant reply and answers:
```
Your name is Piyali.
```
Without the assistant message (or other prior context), it would not know what happened previously.

## 4. role: "tool"
This role contains the output of a tool that the agent invoked.

Suppose the user asks:
```
Latest Angular version?
```
The flow is:
```
User
↓
Gemini
↓
Calls Tavily
↓
Tavily returns data
↓
Gemini reads tool output
↓
Final answer
```
The conversation might look like this:
```
[
    {
        role: "user",
        content: "Latest Angular version?"
    },
    {
        role: "assistant",
        content: "I'll search the web."
    },
    {
        role: "tool",
        content: "Angular 20.1 released..."
    },
    {
        role: "assistant",
        content: "Angular 20.1 is the latest release..."
    }
]
```
The user doesn’t usually create tool messages. The agent framework creates them automatically.

## 5. role: "function"
Historically, OpenAI models used a function role when calling functions. Many modern frameworks instead use tool.

Example:
```
{
    role: "function",
    name: "getWeather",
    content: "{\"temperature\":30,\"city\":\"Kolkata\"}"
}
```
The model then responds:
```
The current temperature in Kolkata is 30°C.
```
In modern LangChain/LangGraph applications, you’ll usually encounter tool rather than function.

## 6. role: "error"
This is not a standard role in the Gemini or OpenAI chat APIs. Some frameworks introduce it internally to represent failures.

Example:
```
{
    role: "error",
    content: "Tavily API timeout."
}
```
An agent might then decide to answer:
```
The search service is currently unavailable. Here's what I know from my existing knowledge...
Whether error is available depends on the framework you're using.
```
Complete Agent Conversation
A ReAct agent’s conversation often evolves like this:
```
┌────────────────────────────────────────────┐
│ System                                    │
│ You are an AI research assistant.         │
└────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────┐
│ User                                      │
│ Latest Angular version?                   │
└────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────┐
│ Assistant                                 │
│ I'll search the web.                      │
└────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────┐
│ Tool                                      │
│ Angular 20.1 released...                  │
└────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────┐
│ Assistant                                 │
│ Angular 20.1 is the latest version...     │
└────────────────────────────────────────────┘
```

## Which roles will you use most?
When building agents with Node.js + LangChain + LangGraph + Gemini, these are the roles you’ll encounter most frequently:

| Role        | Who creates it?             | Purpose                                                                        |
| ----------- | --------------------------- | ------------------------------------------------------------------------------ |
| `system`    | Developer                   | Sets the assistant's behavior, rules, and instructions                         |
| `user`      | Human                       | Provides questions or requests                                                 |
| `assistant` | LLM                         | Stores the model's responses for conversation history                          |
| `tool`      | Agent framework             | Contains the output of external tools such as Tavily or a calculator           |
| `function`  | Older function-calling APIs | Represents function outputs; largely superseded by `tool` in modern frameworks |
| `error`     | Framework-specific          | Represents tool or workflow errors if the framework supports it                |
For modern LangGraph-based applications, you’ll spend most of your time working with system, user, assistant, and tool messages. The ReAct agent manages the assistant and tool messages for you, while you typically provide the system and user messages.

## Are these roles only applicable for Gemini/OpenAI ?
No. These roles are not specific to Gemini or OpenAI. They are part of the chat conversation abstraction used by many modern LLMs and AI frameworks. However, the exact supported roles vary by model provider and API.

| Model/Framework          | system | user | assistant |   tool  |    function    | Notes                                                            |
| ------------------------ | :----: | :--: | :-------: | :-----: | :------------: | ---------------------------------------------------------------- |
| OpenAI Chat Completions  |    ✅   |   ✅  |     ✅     |    ✅    |     Legacy     | `function` has largely been replaced by `tool`.                  |
| Google Gemini            |    ✅   |   ✅  |     ✅     |    ✅    |        ❌       | Uses tool/function calling APIs, but not a `function` chat role. |
| Anthropic Claude         |    ✅   |   ✅  |     ✅     |    ✅    |        ❌       | Supports tools, but the API format differs from OpenAI.          |
| Meta Llama (chat models) |    ✅   |   ✅  |     ✅     | Depends |        ❌       | Native models don't define tools; frameworks add them.           |
| Mistral                  |    ✅   |   ✅  |     ✅     |    ✅    |        ❌       | Tool calling is supported in recent APIs.                        |
| Cohere Command           |    ✅   |   ✅  |     ✅     |    ✅    |        ❌       | Supports tool use.                                               |
| LangChain                |    ✅   |   ✅  |     ✅     |    ✅    | Legacy support | Provides a unified interface across providers.                   |
| LangGraph                |    ✅   |   ✅  |     ✅     |    ✅    | Legacy support | Internally uses message classes rather than raw role strings.    |

## The important distinction

There are three layers involved:
```
                 Your Application
                        │
                        ▼
         LangChain / LangGraph Messages
                        │
                        ▼
          Provider API (Gemini/OpenAI/etc.)
                        │
                        ▼
                     LLM Model
```
The message roles you write in your application are not always sent unchanged to the model. LangChain often converts them into the format expected by the specific provider.

**Example with Gemini**

You write:
```
messages: [
  {
    role: "system",
    content: "You are a Java expert."
  },
  {
    role: "user",
    content: "Write Hello World."
  }
]
```
LangChain converts these into Gemini's internal request format before sending them.

**Example with Claude**

You can write exactly the same LangChain code:
```
messages: [
  {
    role: "system",
    content: "You are a Java expert."
  },
  {
    role: "user",
    content: "Write Hello World."
  }
]
```
But LangChain transforms it into Anthropic's expected API structure.

**Example with OpenAI**

Again, your application code stays the same:
```
messages: [
  {
    role: "system",
    content: "You are a Java expert."
  },
  {
    role: "user",
    content: "Write Hello World."
  }
]
```
LangChain converts it into OpenAI's chat completion request.

**Without LangChain**

If you call provider APIs directly, the formats differ.

**OpenAI**
```
const response = await client.chat.completions.create({
  model: "gpt-5",
  messages: [
    {
      role: "system",
      content: "You are a Java expert."
    },
    {
      role: "user",
      content: "Write Hello World."
    }
  ]
});
```

**Gemini**

The native API uses a different structure (conceptually):
```
const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          text: "Write Hello World."
        }
      ]
    }
  ]
});
```
Notice that Gemini's native API doesn't mirror OpenAI's messages format exactly.

## Why LangChain exists

**Without LangChain, you'd need different code for every provider.**
```
OpenAI API
    │
Different request

Gemini API
    │
Different request

Claude API
    │
Different request

Mistral API
    │
Different request
```

**With LangChain:**
```
Your Code
      │
      ▼
LangChain Messages
      │
      ▼
Converts to
      │
 ┌────┼────┬─────┐
 ▼    ▼    ▼     ▼
GPT Gemini Claude Mistral
```
You change only the model class, while the rest of your application can remain largely unchanged.

## Where does tool come from?

tool isn't owned by OpenAI or Gemini. It's part of the agent workflow.
```
User

↓

LLM

↓

Needs Calculator?

↓

Needs Search?

↓

Needs Database?

↓

Tool Executes

↓

Tool Message

↓

LLM Reads Tool Result

↓

Assistant Response
```
This pattern is common across modern providers that support tool calling.

## Which roles should you learn today?

If you're building modern AI agents with LangChain or LangGraph, focus on these:
```
System
    │
    ▼
User
    │
    ▼
Assistant
    │
    ▼
Tool
```
These four roles form the backbone of contemporary agent applications across Gemini, OpenAI, Claude, Mistral, and other major providers. function is mainly useful for understanding older OpenAI examples, while error is an application-level concept rather than a standard LLM conversation role.