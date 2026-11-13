# Knowledge vs Context vs Procedural Graph

## 📌 Each question needs its own graph.

- **Knowledge Graph: "What is true?"**
Passengers, flights, fares, routes.
Stable, governed, enterprise-wide.

- **Context Graph: "What matters right now?"**
Gate change. Four seats left. Nine minutes to close.
A dozen nodes scoped to this decision, plus the trace of how similar cases went.

-  **Procedural Graph: "What do I do next?"**
(procedure, relation, procedure) triplets.
Check availability → Compare → Rebook. Check visa, if required.

## 📌 What breaks when one is missing

- No knowledge graph: the agent has nothing reliable to stand on.
- No context graph: it searches 40,000 nodes by similarity to find the six that count. That's retrieval, not reasoning.
- No procedural graph: it generates over a growing history. On long tasks it loses the goal, calls tools out of order, and loops.

## 📌 How they connect in production Request: "Rebook this passenger."

1. Procedural graph finds the step: Check Availability.
2. Context graph pulls only what that step needs from the knowledge graph: this flight, 4 seats, Gate C8.
3. Agent acts, guided by the next edge, free to deviate.
4. The trace is written back. 

**Each loop makes all three better:**
- Traces give the next decision precedent
- Failed runs fix the procedure
- Repeated patterns become governed facts

## 📌 Production takeaways

- Don't hand the agent the whole graph. Scope it per step.
- Store the procedure as a graph, not a prompt.
- Log every decision. That's your audit trail.

## 📌 The Semantic Spine

- Meaning - ontology. What things are.
- Facts - knowledge graph. What's true.
- Context - context graph. What matters now.
- Procedure - procedural graph. What to do next.
- Action - the agent. Acting on it, then learning from it.







