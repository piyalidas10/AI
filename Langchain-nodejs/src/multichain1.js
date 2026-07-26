import { config } from "dotenv";
config();

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { RunnableParallel } from "@langchain/core/runnables";

// 1. Create the model
const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  temperature: 0.7,
  maxOutputTokens: 2048,
  apiKey: process.env.GOOGLE_API_KEY,
});

// 2. Prompt
// 3. Create LCEL chain
// A better practice is to add an output parser.

// RunnableParallel allows you to create a map of chains that can be invoked in parallel with a single input object.
/**
 * Execution Flow
 * 
            { topic: "cats" }
                    │
                    ▼
          RunnableParallel
           ┌────────┴────────┐
           ▼                 ▼
      Joke Prompt       Poem Prompt
           │                 │
           ▼                 ▼
        Gemini            Gemini
           │                 │
           ▼                 ▼
     StringParser      StringParser
           └────────┬────────┘
                    ▼
              Combined Output

  Both prompts execute at the same time, making this faster than running them sequentially.
 */
const parallelChain = RunnableParallel.from({
  joke: PromptTemplate.fromTemplate(
    "Tell me a joke about {topic}"
  ).pipe(model).pipe(new StringOutputParser()),

  poem: PromptTemplate.fromTemplate(
    "Write a 2-line poem about {topic}"
  ).pipe(model).pipe(new StringOutputParser()),
});

// 4. Invoke
// Now returns a plain string instead of an AIMessage because of the output parser.
const response = await parallelChain.invoke({
  topic: "cats"
});

console.log(response);

/**
 ***********************************Answers*************************************************
 * {
    poem: 'With a purr and a graceful leap,\nSecrets in their eyes they keep.',
    joke: 'What do you call a cat that eats lemons?\nA sour-puss!'
  }
 */