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
const prompt = PromptTemplate.fromTemplate(
  "Translate the following to French: {text}"
);

// 3. Create LCEL chain
// A better practice is to add an output parser.
const chain = prompt
  .pipe(model)
  .pipe(new StringOutputParser());

// 4. Invoke
// Now returns a plain string instead of an AIMessage because of the output parser.
const response = await chain.invoke({
  text: "Hello"
});

console.log(response);

/**
 ***********************************Answers*************************************************
 * Bonjour
 */