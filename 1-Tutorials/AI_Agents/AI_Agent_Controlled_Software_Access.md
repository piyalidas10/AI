# AI Agent Can't Directly Connect to the Internet & Download Software

Yes, in this architecture, an AI agent running inside the sandbox cannot directly access the Internet to download software or dependencies. Instead, it must go through an approved enterprise artifact repository called **JFrog Artifactory**.

The objective is to prevent an AI agent from downloading malicious packages, unauthorized software, or unverified dependencies.

## 1. How the architecture works

There are two main environments:

### A. Agent Sandbox

The sandbox contains:

- **Agent Run:** Executes the AI agent.
- **Install Dependencies:** Allows the agent to install required libraries and packages.
- **Network restrictions:** Blocks direct Internet access.

For example, suppose the AI agent needs to install:

```bash
pip install fastapi
npm install express
```

The agent cannot directly download these packages from PyPI or npm. Instead, its package manager must communicate with the approved Artifactory repository.

### B. Artifactory (Enterprise Package Gateway)

Artifactory acts as a controlled gateway between the sandbox and the Internet.

It contains four important components:

| Component | Responsibility |
|---|---|
| Virtual Repository | Single approved endpoint for package requests |
| Private Packages | Internally approved enterprise packages |
| Upstream Cache | Stores externally downloaded packages |
| Scan and Policy | Checks packages against security policies |

## 2. Real-time example: AI agent installs FastAPI

Imagine an AI agent needs FastAPI to execute a Python application.

1. **Agent requests a dependency**

   ```bash
   pip install fastapi
   ```

   The request originates inside the sandbox.

2. **Request goes to Artifactory Virtual Repository**

   The package manager is configured to use the enterprise repository instead of the public PyPI endpoint.

3. **Artifactory checks Private Packages**

   Is FastAPI already available in the organization's private repository?

   - Yes: Retrieve the approved package.
   - No: Check the upstream cache.

4. **Upstream Cache checks for the package**

   - Cache hit: Reuse the previously cached package.
   - Cache miss: Retrieve it from the configured upstream registry.

5. **Security scanning and policy validation**

   Check the package for vulnerabilities, malicious content and policy violations.

6. **Approved package reaches the agent**

   Artifactory serves the package to the sandbox. The agent can now install and use it.

## 3. What happens if a package is malicious?

For example, the AI agent requests:

```bash
pip install suspicious-package
```

Suppose the package contains malicious code.

1. Artifactory retrieves the package through its approved upstream mechanism.
2. Security scanning identifies a policy violation.
3. The package is blocked.
4. Artifactory does not serve the package to the agent.
5. The installation fails.

The AI agent cannot bypass this restriction by directly connecting to the Internet, assuming the sandbox's network restrictions are correctly enforced.

## 4. Who controls what?

| Action | AI Agent | Artifactory |
|---|---|---|
| Request dependency | Allowed | |
| Direct Internet download | Blocked | |
| Access private packages | Requests access | Controls access |
| Download upstream packages | | Controls retrieval |
| Cache dependencies | | Yes |
| Scan packages | | Yes |
| Enforce package policies | | Yes |

## 5. Important enterprise security considerations

Artifactory does **not** automatically make every package safe.

A production implementation should also enforce:

- Network-level egress restrictions on the sandbox.
- Package allowlisting and approved registries.
- Malware and vulnerability scanning.
- Dependency pinning and version control.
- Package integrity verification using hashes/signatures.
- Audit logs for every dependency request.
- Restrictions on alternate download mechanisms such as `curl`, `wget`, and direct Git downloads.

## Key concept

```text
AI Agent → Artifactory → Security Validation → Approved Package
```

The AI agent can request and install software, but it does not receive unrestricted Internet access. The enterprise repository controls which external dependencies are allowed into the sandbox.

This is an example of **controlled software supply-chain access for autonomous AI agents**. It is especially important in enterprise environments where AI agents can execute shell commands, install dependencies, and run arbitrary code.
