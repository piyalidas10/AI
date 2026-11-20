# Multi-agent architecture with a central orchestrator

I would not create eight independent chatbots. Instead, I would create one central orchestrator that delegates work to specialized agents.

## Here is the logical architecture:

```Mermaid
flowchart TB
    U["Visitor / Tourist"]
    UI["Angular 19 Web / Mobile PWA"]
    GW["API Gateway - FastAPI"]
    AUTH["Authentication and Session"]
    ORCH["AI Agent Orchestrator"]

    U --> UI --> GW --> AUTH --> ORCH

    ORCH --> PD["Pandal Discovery Agent"]
    ORCH --> RP["Route Planning Agent"]
    ORCH --> CI["Crowd Intelligence Agent"]
    ORCH --> CG["Cultural Guide Agent"]
    ORCH --> FS["Food and Facilities Agent"]
    ORCH --> SA["Safety Agent"]
    ORCH --> EA["Event Agent"]

    PD --> TOOLS["MCP / Tool Layer"]
    RP --> TOOLS
    CI --> TOOLS
    CG --> TOOLS
    FS --> TOOLS
    SA --> TOOLS
    EA --> TOOLS

    TOOLS --> MAP["Maps and Routing API"]
    TOOLS --> DB["PostgreSQL / PostGIS"]
    TOOLS --> CROWD["Crowd and Traffic Feeds"]
    TOOLS --> RAG["RAG / Qdrant"]
    TOOLS --> EVENTS["Event and Transit APIs"]

    ORCH --> LLM["LLM Provider"]
    RAG --> LLM

    ORCH --> RESP["Response Aggregator"]
    RESP --> UI
```

## How the orchestrator works
Suppose the visitor asks:

"Find five famous pandals in South Kolkata and plan a route for my family."

The orchestrator:
1. Classifies the request as discovery + route planning.
2. Extracts location, number of pandals and family constraints.
3. Invokes the Pandal Discovery Agent.
4. Receives verified pandal information.
5. Invokes Crowd Intelligence Agent.
6. Invokes Route Planning Agent.
7. Validates the route and travel estimates.
8. Combines everything into one response.
The LLM decides which tools to invoke, but actual route distances, schedules and location data should come from deterministic services.