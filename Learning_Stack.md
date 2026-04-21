# AI Learing Stack

## Tutorials
1. GenAI For Developers Roadmap 2025 : https://www.youtube.com/watch?v=v1pj9XrJ_Lw
2. Choosing an AI Career in 2026? Understand Every AI Role Before You Start | CampusX : https://www.youtube.com/watch?v=99KPe5hIfnE
3. How to Become an AI Engineer in 2026 - Full Roadmap : https://www.youtube.com/watch?v=r00avsdlEkI
4. AI Engineer Complete RoadMap for 2026 | from basics to AI/ML Advanced : https://www.youtube.com/watch?v=t9MJ1gxcJ4w
5. 20 AI Concepts Explained in 40 Minutes : https://www.youtube.com/watch?v=OYvlznJ4IZQ

## Contents
1. LLM with hyperparameter. hyperparameter is two types :
   - Prompting
     - Prompt hyperparameters include temperature, top_p, top_k, preamble/system prompts
   - Finetuning
2. AI Model are two types
   - Decoder model like Anthropic Claude Sonnet
   - Encoding model
3. prompt engineering
4. context engineering
5. RAG
6. MCP
7. Google A2A
8. Responsible AI

### Prompting
start prompting. send the different prompt via langchain/ langgraph to ollama
1. create front end container 
2. docket setup with 5 container
a) UI container 
b) Ekta FastAPI ba kono Rest APi server container  
c) Ollama container 
d) ekta Vector DB container like FAISS / QDrant  
e) ekta No sql container like Mongo to store the prompt and results

Ollama is not a LLM it is a llm management system

Now try to fine tune the tags and other ways , to modify semantic search and keep it in a boundary

Go in depth like multitenant operation in qdrant

### Food Discovery Demo - Qdrant
learn about different embedding , like ada03
food-discovery-demo : https://qdrant.tech/articles/food-discovery-demo/

- qdrant.tech
- look this , non Gen AI apps
- go in deep e jao and see different use cases
- also start integrating a MCP server with langchain or langgraph

### MCP
this is next step , like when i am sending.a prompt it should look at RAG + MCP

https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/

- Catalog
- docs.docker.com
- docker has published lot of MCP servers , now make the Langchain / langgraph talk with MCP as well as RAG
- MCP server lists (https://hub.docker.com/mcp/explore)
- qdrant vector db ( all functionality explore)
- faiss  vector db ( all functionality explore)

langgraph can be used for MCP server integration , whether langchain will suffice or agno or langgraph is needed do a feasability study

### agno api
https://docs.agno.com/introduction

### How to convert your FastAPI RAG system into an MCP-enabled AI platform

✅ Full Production Hybrid RAG (Ollama + Qdrant + FastAPI + Docker)
✅ Agentic RAG (AutoGen / LangGraph) ← trending
✅ MCP + RAG integration (next-gen systems)

### Build
• AI resume tool
• Smart dashboard
• Automation app

### Enterprise RAG Platform (Guardrails + Self-Healing + Monitoring)
Built a production-grade Advance RAG system using FastAPI, Qdrant, Ollama, and LangChain, enhanced with guardrails, trust scoring, observabi

### how to invoke agent and write custom github agents
1. **how to invoke agent and write custom github agents :** For example, suppose you have a repository, and inside VS Code you can call an agent. Then you provide it with a set of instructions about what needs to be done with your repo.
   - https://docs.github.com/en/copilot/reference/custom-agents-configuration
   - https://docs.github.com/en/copilot/reference/custom-instructions-support
3. it cointains some ways by which Agent is evaluated : https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html
4. LLM Evaluation is different from Agent Evaluation : https://github.com/confident-ai/deepeval

>  tobe tinte dike jacche AI ta job e , ekta hocche custom agent use kore github copilot e 1 day r kaj 30 min e kora , ar ar ekta hocche core application develop kora , mane LLM development ba notun Time seriees based LLM kind of hard core programming jate indian ra pray nei .. oi sob tensorflow. pytorch keras ar c binding for NVDIA and other GPU , third hocche tumi ja korcho , AI application stack with agent building , guardrail LLM evaluation , LLM context and LLM fine tuning

### Impact on CV
Including LLM evaluation in the CV is valuable. When working with smaller LLMs (e.g., via Ollama), the outputs can often be inconsistent or incorrect, so a robust evaluation layer is essential to catch errors and ensure reliability.

If you want a more impactful CV bullet, you can write it like this:
- Built an LLM evaluation pipeline to validate model outputs and detect hallucinations, ensuring response accuracy and reliability.
- Implemented evaluation frameworks for local LLMs (Ollama-based) to handle noisy and inconsistent outputs.
- Designed automated quality checks (accuracy, relevance, safety) for AI-generated responses.

