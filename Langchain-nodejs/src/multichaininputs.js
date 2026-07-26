import { config } from "dotenv";
config();

import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";

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
const jokeChain = PromptTemplate
  .fromTemplate("Tell me a joke about {topic}")
  .pipe(model)
  .pipe(new StringOutputParser());

const poemChain = PromptTemplate
  .fromTemplate("Write a two-line poem about {topic}")
  .pipe(model)
  .pipe(new StringOutputParser());

// 4. Invoke
// Now returns a plain string instead of an AIMessage because of the output parser.
const [joke, poem] = await Promise.all([
  jokeChain.invoke({ topic: "cats" }),
  poemChain.invoke({ topic: "sunsets" }),
]);
console.log({ joke, poem });

/**
 ***********************************Answers*************************************************
 * {
    joke: 'Why did the cat sit on the computer?\n' +
        '\n' +
        'Because it wanted to keep an eye on the mouse!',
    poem: 'Gold and crimson paint the fading light,\n' +
        'A masterpiece before the coming night.'
    }
 */