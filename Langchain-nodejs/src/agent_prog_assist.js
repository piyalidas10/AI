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
    Search the latest documentation for Angular Signals.

    Explain them with a code example.
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
[
  {
    type: 'text',
    text: 'Angular Signals are a new reactivity model in Angular designed for intuitive, precise, and clear state management, enabling very fine-grained updates to the DOM. They aim to optimize change detection and re-rendering by allowing Angular to determine exactly what parts of the page need to be updated, rather than checking all components.\n' +
      '\n' +
      'Unlike the traditional RxJS approach with observables, operators, and `async` pipes, Signals offer a simpler API for reporting and tracking data changes. They eliminate the need for pipes, `subscribe` calls, and manual teardown.\n' +
      '\n' +
      'The core API for Angular Signals consists of three main primitives:\n' +
      '\n' +
      '*   **`signal(initialValue)`**: Creates a writable reactive value. This is the fundamental building block for creating a piece of state that can change over time.\n' +
      '*   **`computed(fn)`**: Derives a new value from one or more existing signals. The `computed` value automatically updates whenever any of its dependent signals change.\n' +
      '*   **`effect(fn)`**: Runs a side-effect whenever its dependent signals change. Effects are typically used for synchronizing state with the DOM, logging, or other non-rendering logic.\n' +
      '\n' +
      "Here's a code example demonstrating `signal` and `computed`:\n" +
      '\n'
  },
  {
    type: 'text',
    text: '```typescript\n' +
      "import { signal, computed, effect } from '@angular/core';\n" +
      '\n' +
      '// 1. Create a writable signal\n' +
      'const count = signal(0);\n' +
      '\n' +
      "// 2. Create a computed signal that depends on 'count'\n" +
      'const doubleCount = computed(() => count() * 2);\n' +
      '\n' +
      '// 3. Create an effect to react to changes\n' +
      'effect(() => {\n' +
      '  console.log(`Current count: ${count()}, Double count: ${doubleCount()}`);\n' +
      '});\n' +
      '\n' +
      '// Initial values\n' +
      "console.log('Initial count:', count()); // Output: Initial count: 0\n" +
      "console.log('Initial doubleCount:', doubleCount()); // Output: Initial doubleCount: 0\n" +
      '\n' +
      "// Update the 'count' signal\n" +
      'count.set(5);\n' +
      '// The effect will run automatically:\n' +
      '// Output: Current count: 5, Double count: 10\n' +
      '\n' +
      "// Update 'count' again\n" +
      'count.update(currentCount => currentCount + 1);\n' +
      '// The effect will run automatically:\n' +
      '// Output: Current count: 6, Double count: 12\n' +
      '\n' +
      '// You can also read the current value of a signal\n' +
      "console.log('Updated count:', count()); // Output: Updated count: 6\n" +
      '```'
  },
  {
    type: 'text',
    text: '\n' +
      '\n' +
      'In this example:\n' +
      '*   `count` is a signal initialized to `0`. Its value can be changed using `set()` or `update()`.\n' +
      '*   `doubleCount` is a computed signal that automatically recalculates its value (`count() * 2`) whenever `count` changes.\n' +
      '*   The `effect` logs the current values of `count` and `doubleCount` whenever either of them changes. This demonstrates how effects react to signal changes.'
  }
]
--------------------------------
 */