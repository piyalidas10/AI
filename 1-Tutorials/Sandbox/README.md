# AI Agent Sandboxing

This lecture explains an important AI Agent security concept: **Sandboxing** – controlling where an AI agent can execute tools and access files.

Let's break it down with practical examples, especially from an enterprise AI application development perspective.

<img src="./AI Agent Sandboxing Explained.png" width="100%" />

## 1. Where are AI agent tools executed?

When an LLM uses a tool, the tool is generally executed by the environment running the agent, not by the LLM itself.

For example, suppose you build an AI agent that can:

- Read files.
- Create files.
- Delete files.
- Execute Python scripts.
- Run terminal commands.

The architecture looks like this:

```text
User
  "Create a report from my documents"
        |
        v
LLM
  Decides which tool to call
        |
        v
AI Agent Runtime
  Receives tool call and executes it
        |
        +--> File System: Read / Write files
        |
        +--> Terminal: Execute commands
```

Important distinction:

- **LLM** decides what action should happen.
- **Agent runtime** executes the action.
- **Operating environment** determines what resources the action can access.

## 2. What is sandboxing?

Sandboxing means running an application or process inside an isolated environment with restricted access to the host system.

Imagine your computer has these folders:

```text
My Computer
│
├── Documents
│   ├── Personal/
│   └── Banking/
│
├── Projects
│   ├── Angular/
│   └── Python/
│
├── Downloads/
│
└── System Files/
```

Suppose you give an AI agent access only to:

```text
Projects/Angular/
```

The agent can:

- Read Angular project files.
- Create new components.
- Modify TypeScript files.
- Delete files inside its permitted workspace.

Ideally, it cannot:

- Read Personal documents.
- Access Banking documents.
- Modify Windows system files.
- Delete files outside its permitted workspace.

### Sandbox isolation concept

| Zone | Resources | Agent access |
|------|-----------|--------------|
| **Sandbox:** `Projects/Angular/` (Allowed) | `app.component.ts`, `app.routes.ts`, `package.json`, `src/` | Agent can read, write and modify permitted files. |
| **Outside sandbox** (Restricted) | `Documents/Personal/`, `Documents/Banking/`, `Windows/System32/` | Agent should not be able to access these resources. |

## 3. What happens without sandboxing?

Consider this scenario.

You build an AI coding agent using an LLM.

You ask:

> "Clean up my Angular project and remove unnecessary files."

The LLM decides to execute:

```bash
rm -rf *
```

If the agent runs this command with unrestricted permissions, it could delete everything within its current working directory.

An even more dangerous situation occurs if the agent has access to sensitive directories or elevated system privileges.

With proper sandboxing:

- The agent operates within an isolated workspace.
- Files outside its permitted environment are inaccessible.
- Destructive commands are restricted by filesystem and execution permissions.

> **Remember:** Sandboxing reduces the potential damage. It does not guarantee complete security.

## 4. Different ways to implement sandboxing

There are several technical approaches.

| Technique | How it works |
|-----------|--------------|
| Folder-level permissions | Restricts access to specified folders |
| Docker containers | Isolates processes and filesystems |
| Virtual machines | Provides stronger isolation using a separate virtual OS |
| OS sandboxing | Uses operating-system security mechanisms |
| Restricted execution environments | Limits commands, resources and system access |

- **Docker container:** An agent can execute tools inside a container with restricted filesystem mounts, capabilities and networking.
- **Virtual machine:** Runs a separate guest operating system, providing an additional isolation boundary.
- **OS-level sandbox:** Uses mechanisms such as Linux namespaces, seccomp, and AppArmor to restrict processes.

## 5. Practical example: Your local AI Agent project

Suppose you build an AI coding agent using:

- Angular 19 frontend
- FastAPI backend
- Ollama (local LLM)
- Docker
- Python tool execution

**Without sandboxing:**

```text
Angular UI
    |
FastAPI Agent
    |
Ollama LLM
    |
Tool Executor
    |
Your Windows File System
    |
Full or excessive access
```

**With sandboxing:**

```text
Angular UI
    |
FastAPI Agent
    |
Ollama LLM
    |
Tool Executor
    |
Docker Sandbox
    |
/workspace
    |
Only permitted project files
```

For example, your Docker container might mount only the project directory:

```yaml
services:
  ai-agent:
    image: python:3.12-slim

    volumes:
      - ./workspace:/workspace

    working_dir: /workspace

    user: "1000:1000"

    read_only: true

    tmpfs:
      - /tmp

    cap_drop:
      - ALL

    security_opt:
      - no-new-privileges:true
```

This is an illustrative starting point, not a complete production sandbox. You would need carefully configured writable directories, network restrictions, resource limits and other controls.

## 6. Important enterprise security considerations

Sandboxing alone is not enough.

For a production banking AI agent, consider these additional controls:

| Security control | Purpose |
|------------------|---------|
| Least privilege | Give the agent only the permissions it needs |
| Sandboxing | Restrict execution environment |
| Human approval | Require approval for sensitive actions |
| Audit logging | Track every tool invocation |
| Network restrictions | Prevent unauthorized external communication |
| Input validation | Validate tool arguments |
| Secret management | Prevent exposure of credentials |
| Resource limits | Prevent CPU, memory and disk abuse |

For example, a banking agent should never be allowed to execute an unrestricted database deletion just because an LLM generated that tool call.

## 7. Test your understanding

**Knowledge check**

**1. Where does an AI agent typically execute a tool call?**

- Inside the LLM neural network
- **In the agent runtime/environment** ✅
- Inside the user's browser in every case

*Correct: The LLM generates a tool call. The agent runtime executes it.*

**2. What is the main purpose of sandboxing?**

- Make the LLM more intelligent
- Increase token context window
- **Isolate execution and restrict resource access** ✅

*Correct: Sandboxing limits what an agent can access or modify.*

**3. Does Docker automatically guarantee complete isolation?**

- Yes, always
- **No, it needs security configuration** ✅
- Yes, if the container is running

*Correct: Container isolation depends on configuration, host security and the threat model.*

## Key takeaway

The most important distinction to remember:

- **LLM:** Decides what tool should be called.
- **Agent runtime:** Executes the tool.
- **Sandbox:** Restricts where and how the tool executes.
- **Host system:** Contains the actual resources that need protection.

**Recommendation for your local AI Agent learning project:** Build a simple FastAPI + Ollama agent that can read, create and modify files inside a Docker-mounted `/workspace` directory, then test whether it can access files outside that directory. This is an excellent hands-on way to understand agent security.

## 8. How can a user know where the sandbox is?

This is an important part of AI Agent UX (User Experience) and Security Transparency.

The user should not have to guess where the sandbox is. The agent application should explicitly show the user which environment it is operating in and which files or folders it can access.

### 8.1 What does a user see?

Suppose a user opens Claude Code or your custom AI coding agent. The application could show something like:

```text
AI Coding Agent

Sandbox active
Execution environment

Workspace location
  C:/Users/User/AI-Projects/workspace

Folder permissions
  Restricted
  workspace/            Read / Write
  Personal Documents/   Blocked
  Banking/              Blocked

Execution type
  Docker container
```

> *Illustrative UI – not an actual Claude or ChatGPT screenshot.*

This gives the user visibility into the execution environment.

### 8.2 How does the application know where the sandbox is?

The agent application developer configures it.

For example, in your FastAPI + Docker project:

```yaml
services:
  ai-agent:
    image: python:3.12-slim

    volumes:
      - ./workspace:/workspace

    working_dir: /workspace
```

Here:

| Location | Meaning |
|----------|---------|
| `./workspace` | Folder on the host machine |
| `/workspace` | Folder visible inside Docker |
| Docker container | Execution environment |

Your FastAPI backend can expose environment information through an API:

```python
@app.get("/agent/security")
def get_security_info():
    return {
        "sandbox_type": "docker",
        "workspace": "/workspace",
        "filesystem_access": "restricted",
        "read_write": True
    }
```

The Angular frontend can display this information in a Security or Environment panel.

> **Important:** This API response is only descriptive metadata. It must reflect the actual Docker configuration and enforced permissions, not simply claim that the environment is secure.

### 8.3 What happens when the user wants to give access to another folder?

The user asks:

> "Please analyse my Documents folder."

The agent should not silently assume permission. A suitable interaction would be:

```text
Additional folder access requested

Documents/
C:/Users/User/Documents

The AI agent wants permission to read files in this folder.

Access level: Read only
[ Deny ]  [ Approve ]   (user approval required)
```

> *Illustrative permission dialog.*

The backend then updates the permitted mount or access policy after authorization.

### 8.4 Sandbox visibility vs sandbox security

These are two different responsibilities.

| Responsibility | Who handles it? |
|----------------|-----------------|
| Show sandbox location | Agent UI |
| Show permitted folders | Agent UI |
| Enforce filesystem restrictions | Docker / OS |
| Enforce command restrictions | Execution runtime |
| Approve additional access | User + permission system |
| Prevent sandbox escape | Isolation and host security mechanisms |

The UI cannot itself guarantee security. Actual restrictions must be enforced by the execution environment.

### 8.5 How this applies to Claude Code, ChatGPT and your own agent

Different agent products implement execution environments differently. Some use local permissions and filesystem restrictions, others use containers or remote execution environments. The user-facing workspace is not necessarily the physical location of the sandbox.

For your learning, remember this architecture:

| Layer | Role |
|-------|------|
| Angular Frontend | Shows workspace, permissions and security status |
| FastAPI Agent Backend | Validates user permissions and tool requests |
| Sandbox / Docker Runtime | Enforces filesystem, process and network restrictions |
| `/workspace` | Permitted project files |

**Recommendation:** When building your own AI agent, always provide a visible **Security & Permissions** panel. Users should know where the agent works, what it can access, and whether it can read, write, execute or access the network.

That is an important production-ready design principle for enterprise AI agents.

> On sandbox visibility, malware protection is one enterprise security option.

## 9. Workspace selection and permission prompts

When you ask an AI coding agent to open or access a folder, it often asks for your permission before proceeding. This is related to sandboxing and filesystem permissions. There are two scenarios.

### Scenario 1: Initial workspace selection

Suppose you open Claude Code or another coding agent.

1. You select a project folder, for example `Angular19`.
2. The application asks you to trust or authorize access to that folder.
3. You grant permission.
4. The agent uses that folder as its working directory.

```text
User
  |
  v
Open AI Agent
  |
  v
Select Angular19 folder
  |
  v
Permission requested
  |
  v
User approves
  |
  v
Agent works inside Angular19
```

### Scenario 2: Agent wants to access another folder

Suppose the agent is already working inside `Angular19`.

You ask:

> "Read my Python project located in another folder."

The agent attempts to access:

```text
C:/Projects/PythonProject
```

The application may show a permission prompt because this folder is outside the currently authorized workspace. You approve or deny the request.

### What is the relationship?

| Concept | Explanation |
|---------|-------------|
| Workspace | Folder selected for agent work |
| Permission prompt | Asks the user to authorize access |
| Sandbox | Restricts what the agent can access |
| Additional folder access | Expands the agent's permitted resources |

> **Important:** A permission prompt is not itself a sandbox. It is a mechanism for obtaining authorization. The sandbox or operating-system security controls enforce the restriction.

For example, Claude Code has permission modes and filesystem access controls; the exact behavior depends on its configuration.

**Key idea:** The user selects or authorizes the workspace, and the agent operates within the permissions granted to it.
