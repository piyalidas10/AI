import { config } from "dotenv";
config();

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { RunnableMap } from "@langchain/core/runnables";

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

// RunnableMap allows you to create a map of chains that can be invoked with a single input object. 
// Each key in the map corresponds to a chain, and the input object can contain values for each chain's variables.
const mapChain = RunnableMap.from({
  joke: PromptTemplate.fromTemplate(
    "Tell me a joke about {topic}"
  ).pipe(model).pipe(new StringOutputParser()),

  poem: PromptTemplate.fromTemplate(
    "Write a 2-line poem about {topic}"
  ).pipe(model).pipe(new StringOutputParser()),
});

// 4. Invoke
// Now returns a plain string instead of an AIMessage because of the output parser.
const response = await mapChain.invoke({
  topic: "cats"
});

console.log(response);

/**
 ***********************************Answers*************************************************
 * {
    poem: 'With silent grace, they softly tread,\nThen purr and nap upon your bed.',
    joke: 'Why was the cat sitting on the computer?\n\nTo keep an eye on the mouse!'
  }
 */