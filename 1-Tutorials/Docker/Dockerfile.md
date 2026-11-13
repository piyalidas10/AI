# Docker concepts: image layers and build cache

> [!NOTE]  
> Every Dockerfile instruction creates a layer, and Docker caches those layers. If a layer changes, Docker rebuilds that layer and every layer after it.

## 1. Think of the Dockerfile as a stack of layers

**For example:**
```
FROM node:20

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

EXPOSE 80

CMD ["node", "server.js"]
```

**Conceptually:**
```
┌──────────────────────────────┐
│ CMD ["node", "server.js"]    │
├──────────────────────────────┤
│ EXPOSE 80                    │
├──────────────────────────────┤
│ COPY . /app                  │
├──────────────────────────────┤
│ RUN npm install              │
├──────────────────────────────┤
│ COPY package.json /app       │
├──────────────────────────────┤
│ WORKDIR /app                 │
├──────────────────────────────┤
│ FROM node:20                 │
└──────────────────────────────┘
```
Each instruction contributes to the image.

## 2. Docker caches the layers

Suppose you run:
```
docker build -t my-node-app .
```

**The first build might look conceptually like:**
```
FROM node:20          → executed
WORKDIR /app          → executed
COPY package.json     → executed
RUN npm install       → executed
COPY . /app           → executed
EXPOSE 80             → executed
CMD ...               → executed
```

**Now run the same command again:**
```
docker build -t my-node-app .
```

**Docker can say:**
```
FROM node:20          → CACHED
WORKDIR /app          → CACHED
COPY package.json     → CACHED
RUN npm install       → CACHED
COPY . /app           → CACHED
EXPOSE 80             → CACHED
CMD ...               → CACHED
```
So the second build can be dramatically faster.

## 3. What happens when server.js changes?

**Suppose your original Dockerfile is:**
```
FROM node:20

WORKDIR /app

COPY . /app

RUN npm install

EXPOSE 80

CMD ["node", "server.js"]
```

**Initially:**
```
FROM          ✓
WORKDIR       ✓
COPY          ✓
RUN npm       ✓
EXPOSE        ✓
CMD           ✓
```

**Now you modify:**
```
server.js
```

**When Docker reaches:**
```
COPY . /app
```
it detects that the files being copied are different.

**Therefore:**
```
FROM          CACHED
WORKDIR       CACHED
COPY          REBUILD  ← changed
RUN npm       REBUILD  ← after changed layer
EXPOSE        REBUILD
CMD           REBUILD
```

**This is the important rule:**
> [!IMPORTANT]  
> When Docker's cache is invalidated at a layer, subsequent layers also need to be rebuilt.

Docker doesn't simply think:
> "Only server.js changed, therefore npm install isn't necessary."

It doesn't perform that kind of application-level dependency analysis.

## 4. Why COPY package.json separately?

This is the optimization being taught in the lecture.

**Instead of:**
```
COPY . /app
RUN npm install
```

**use:**
```
COPY package.json /app

RUN npm install

COPY . /app
```

**Now your Dockerfile becomes:**
```
FROM node:20

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

EXPOSE 80

CMD ["node", "server.js"]
```

**The layer structure becomes:**
```
FROM node
      ↓
WORKDIR /app
      ↓
COPY package.json
      ↓
npm install
      ↓
COPY source code
      ↓
EXPOSE
      ↓
CMD
```

**Now imagine you modify:**
```
server.js
```

**Docker sees:**
```
FROM node          → CACHED
WORKDIR            → CACHED
package.json       → CACHED
npm install        → CACHED
COPY source code   → REBUILD
EXPOSE             → REBUILD
CMD                → REBUILD
```
Most importantly:

npm install does not run again.

That's the optimization.

## 5. What if package.json changes?

This is where the optimization becomes even clearer.

**Suppose you add a dependency:**
```
{
  "dependencies": {
    "express": "...",
    "axios": "..."
  }
}
```

**Now:**
```
COPY package.json /app
```
detects a change.

**Therefore:**
```
FROM node          → CACHED
WORKDIR            → CACHED
COPY package.json  → REBUILD
npm install        → REBUILD
COPY source code   → REBUILD
EXPOSE              → REBUILD
CMD                 → REBUILD
```
And that's exactly what we want.

Because changing package.json can change your dependencies, so npm install needs to execute again.



