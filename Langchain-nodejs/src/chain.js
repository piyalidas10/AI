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
const prompt = PromptTemplate.fromTemplate(`
You are a helpful assistant.

Question:
{question}
`);

// 3. Create LCEL chain
// A better practice is to add an output parser.
const chain = prompt
  .pipe(model)
  .pipe(new StringOutputParser());

// 4. Invoke
// Now returns a plain string instead of an AIMessage because of the output parser.
const response = await chain.invoke({
  question: "What is the future of AI in healthcare?"
});

console.log(response);

/**
 ***********************************Answers*************************************************
 * 
 * The future of Artificial Intelligence (AI) in healthcare is poised to be profoundly transformative, moving beyond current applications to become an integral part of nearly every aspect of medicine. It won't replace human clinicians but rather augment their capabilities, making healthcare more precise, efficient, accessible, and personalized.

Here are the key areas where AI is expected to revolutionize healthcare:

1.  **Enhanced Diagnosis and Early Detection:**
    *   **Medical Imaging:** AI algorithms will become even more sophisticated at analyzing X-rays, MRIs, CT scans, and pathology slides, identifying subtle anomalies that human eyes might miss. This will lead to earlier and more accurate diagnoses of cancers, neurological conditions, and other diseases.
    *   **Predictive Diagnostics:** By analyzing vast datasets including genomic information, electronic health records, lifestyle data, and environmental factors, AI will be able to predict an individual's risk of developing certain diseases years in advance, allowing for proactive interventions.
    *   **Rare Disease Diagnosis:** AI can sift through complex symptom patterns and genetic data to help diagnose rare diseases much faster, reducing diagnostic odysseys for patients.

2.  **Personalized Treatment and Drug Discovery:**
    *   **Precision Medicine:** AI will enable truly personalized treatment plans by considering an individual's unique genetic makeup, lifestyle, treatment history, and real-time physiological data. This will optimize drug dosages, recommend specific therapies, and predict treatment responses.
    *   **Drug Discovery and Development:** AI will dramatically accelerate the drug discovery process by identifying promising drug candidates, predicting their efficacy and toxicity, optimizing molecular structures, and even designing and managing clinical trials more efficiently. This could reduce the time and cost of bringing new medications to market.
    *   **Gene Editing and Therapy:** AI will assist in identifying optimal gene targets and designing more effective and safer gene-editing strategies.

3.  **Operational Efficiency and Administrative Streamlining:**
    *   **Workflow Optimization:** AI can analyze hospital workflows to identify bottlenecks, optimize staff scheduling, and improve resource allocation, leading to reduced wait times and more efficient patient flow.
    *   **Administrative Tasks:** Automating tasks like medical coding, billing, insurance claims processing, and appointment scheduling will free up healthcare professionals to focus more on patient care.
    *   **Supply Chain Management:** AI can predict demand for medical supplies, optimize inventory, and manage logistics, ensuring hospitals have what they need when they need it.

4.  **Patient Engagement and Remote Care:**
    *   **Virtual Health Assistants and Chatbots:** AI-powered chatbots will provide instant answers to patient questions, assist with symptom checking, guide patients through care pathways, and offer mental health support.
    *   **Remote Patient Monitoring:** Wearable devices and in-home sensors, combined with AI, will continuously monitor vital signs, activity levels, and other health metrics, alerting providers to potential issues before they become critical and enabling proactive interventions.
    *   **Personalized Health Coaching:** AI will offer tailored advice on diet, exercise, and lifestyle modifications based on an individual's health goals and real-time data.

5.  **Preventive Healthcare and Public Health:**
    *   **Population Health Management:** AI will analyze public health data to identify disease outbreaks, predict their spread, and inform public health interventions more effectively.
    *   **Risk Stratification:** Identifying individuals at high risk for chronic diseases or adverse health events, allowing for targeted preventive programs.

6.  **Medical Research and Education:**
    *   **Data Analysis:** AI will be indispensable for analyzing vast and complex medical research data, identifying patterns, generating hypotheses, and accelerating scientific discovery.
    *   **Training Tools:** AI-powered simulations and virtual reality tools will provide immersive and realistic training for medical students and practitioners, allowing them to practice complex procedures and decision-making in a safe environment.

**Challenges and Ethical Considerations:**
Despite the immense potential, the future of AI in healthcare also faces significant hurdles:
*   **Data Privacy and Security:** Protecting sensitive patient data will be paramount.
*   **Algorithmic Bias:** Ensuring AI models are trained on diverse and representative data to avoid perpetuating or exacerbating health disparities.
*   **Regulatory Frameworks:** Developing clear guidelines for AI's use, validation, and oversight in clinical settings.
*   **Interoperability:** Integrating AI tools seamlessly with existing, often fragmented, healthcare IT systems.
*   **Trust and Acceptance:** Gaining the trust of both clinicians and patients will be crucial for widespread adoption.
*   **Cost and Accessibility:** Ensuring that advanced AI healthcare solutions are affordable and accessible to all, not just a privileged few.
*   **Job Displacement/Redefinition:** Healthcare roles will evolve, requiring re-skilling and new types of collaboration between humans and AI.
 */