# API protocols
10 API protocols every engineer needs in the AI era.

7 classic ones. 3 that AI agents rely on now.

Each with when to use it and how it breaks.

## REST
------
↳ Resources + HTTP verbs, stateless
↳ Use: public CRUD APIs
↳ Breaks: retried POSTs create duplicates. Use idempotency keys.


## GraphQL
------
↳ Client asks for exactly the fields it needs
↳ Use: apps with many screens and shifting data needs
↳ Breaks: one deep nested query can flatten your DB. Add depth and cost limits.

## gRPC
------
↳ Typed Protobuf contracts over HTTP/2
↳ Use: service-to-service calls, model inference servers
↳ Breaks: no deadline means one slow service hangs the whole chain.

## WebSockets
------
↳ Two-way, always-open connection
↳ Use: chat, multiplayer, live collaboration
↳ Breaks: connections die silently. Add heartbeats and reconnect logic.

## SSE (Server-Sent Events)
------
↳ Server streams events to the client over plain HTTP
↳ Use: streaming LLM tokens. It's how most chat UIs type word by word.
↳ Breaks: proxies that buffer responses kill the stream.

## Webhooks
------
↳ Another system calls your URL when something happens
↳ Use: payments, long-running AI jobs finishing
↳ Breaks: your endpoint is down and the event is lost. Retries + signatures + idempotent handlers.

## AMQP / MQTT
------
↳ Publish-subscribe through a broker
↳ Use: AMQP for durable work queues. MQTT for IoT on weak networks.
↳ Breaks: at-least-once delivery means duplicates. Consumers must be idempotent.

                                             
## Now the AI layer

### MCP (Model Context Protocol)
------
↳ A standard way for an LLM app to discover and call tools and data. Built on JSON-RPC.
↳ Use: connecting agents to GitHub, Slack, databases, internal APIs
↳ Breaks: a poisoned tool description can inject instructions into the model. Treat every tool as untrusted.

### A2A (Agent2Agent)
------
↳ Agents publish "Agent Cards", discover each other, and hand off tasks
↳ Use: multi-agent systems across teams or vendors
↳ Breaks: tasks run for minutes or hours. You need status tracking, not just request/response.

### WebRTC
------
↳ Low-latency audio, video, and data streams
↳ Use: real-time voice AI agents
↳ Breaks: strict firewalls block direct connections. You need TURN servers.

## The cheat sheet:
→ Client asks, server answers: REST / GraphQL  
→ Service calls service: gRPC  
→ Server pushes, client listens: SSE  
→ Both sides talk nonstop: WebSockets  
→ "Tell me when it's done": Webhooks / queues  
→ Agent needs a tool: MCP  
→ Agent needs another agent: A2A  
→ Agent needs to talk out loud: WebRTC  



