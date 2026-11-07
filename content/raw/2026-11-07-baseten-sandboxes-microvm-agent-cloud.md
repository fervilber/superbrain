---
title: "Baseten Launches Sandboxes for Long-Running, Stateful AI Agents"
source: "https://www.unite.ai/baseten-launches-sandboxes-for-long-running-stateful-ai-agents"
date: 2026-11-07
captured: 2026-11-07T20:06:00+01:00
---

# Baseten Launches Sandboxes for Long-Running, Stateful AI Agents

Baseten introduced Sandboxes on November 5, 2026, giving AI agents isolated microVM environments that preserve files, memory and running processes between tasks. The execution service is available now and free to use until November 16, 2026, as the first component of Baseten's planned agent cloud.

The product documentation sets a default limit of 10 concurrent sandboxes per organization, with support able to raise it. Teams can assign separate environments to individual users or projects and create or delete them as users and projects change. Example uses include an agent writing and running a website's code for a user, or downloading sources, analyzing them and collecting research results.

## MicroVM Isolation and Saved State

The isolation boundary is a dedicated microVM for every environment, with a separate kernel and hardware-level isolation. Baseten says this provides more isolation than container-based approaches and lets agents execute untrusted code, manipulate files and run processes without lateral movement. The state system addresses a different problem: preserving progress without continuously running compute.

Disconnection triggers a snapshot covering the filesystem, memory and active processes. Compute scales to zero while the environment sleeps; resuming restores its saved state so work can continue across sessions or pause for human input. This makes suspension both a continuity feature and a resource-management mechanism: numerous workspaces can remain saved while active compute is reserved for environments doing work.

Baseten reports a 25-millisecond resume time, scaling to thousands of sandboxes within seconds, and a speed advantage of up to five times over other sandboxing tools. The latency target is cumulative: startup, file reads and writes, and inference round trips can otherwise compound across long agentic loops.

The dashboard includes live API-request, error-rate, CPU and memory metrics, along with deployment details such as region, RAM, image and labels. The built-in observability shows what an agent's environment is doing without requiring a separate monitoring setup.

## Images, Access and Data Retention

Every sandbox starts from an image. Baseten maintains built-in options, while teams can build custom images from a Dockerfile or import them from a registry, with versions managed per team. An image can contain operating-system and language runtimes, packages and command-line tools, starting code or data, and default memory and port settings. A Sandbox API server handles commands and file operations for MCP tools.

After a custom image builds successfully, it receives a tagged version, and each new sandbox starts from a copy of that version. Files created or changed during a run do not modify the image. Developers can create environments through the Baseten CLI, execute commands or open an interactive terminal, and coding agents can use those same CLI commands.

Saved state has a deletion boundary. Deleting a sandbox, including deletion when it expires, permanently removes its local data. Results must be saved outside the environment or retained on a mounted sandbox volume to survive across sandboxes.

## Storage and Networking Remain on the Roadmap

Baseten's architectural premise is that earlier cloud primitives were built for one application serving millions of users, while agents invert that model into millions of micro-applications serving a handful of human or agent users. Each environment then needs its own tools, accumulated work and files, supported by compute, storage, networking and identity designed together.

Sandboxes join Dedicated Inference, Model APIs, Training, Loops and Grid in Baseten's platform, adding execution to its inference, training, routing and governance products. For storage, Agent Drive would provide a distributed remote filesystem shared across sandboxes, optimized for high write volumes and small files such as code and Markdown. Agent Proxy would enforce connection rules outside the sandbox and inject credentials during sensitive calls, such as a Stripe payment, without exposing those credentials to the agent. The broader design includes permissions, audit logging, firewalling, static IPs and configurable controls. Baseten expects Agent Drive and Agent Proxy to come online in the coming months.

The practical boundary is that Sandboxes can preserve an agent's working state across pauses, but results that must survive deletion still require storage outside the environment or a mounted volume. The shared filesystem and externally enforced credential controls remain roadmap items, so the agent cloud currently begins with execution rather than the full compute, storage and networking system Baseten describes.

## Notas de anuncio oficial y cobertura secundaria

- X/Baseten (5 de noviembre de 2026, 17:32): "As we build towards the agent cloud, today we introduce Baseten Sandboxes. Isolated environments where your agents work, sitting right next to your inference and training. Everything agents need to act fast, all on one platform. Built on Carbon, our frontier runtime for agentic execution."
- Blog oficial, "Building the Agent Cloud: Introducing Baseten Sandboxes", November 5, 2026: "We're making Baseten Sandboxes free to run until November 16th; Isolated: Sandboxes run on microVMs."
- explainx.ai (5 de noviembre de 2026): los sandboxes entran en standby tras ~30 segundos de inactividad; límite por defecto de 10 sandboxes simultáneos por organización; gratuitos hasta el 16 de noviembre.
- Contexto de mercado (Fastio / Northflank): el aislamiento por microVM (Firecracker, Kata Containers) y el sandboxing de kernel en espacio de usuario (gVisor) ofrecen compromisos distintos de seguridad/rendimiento/compatibilidad. Para agentes de investigación con estado, las sesiones que sobreviven días o semanas son críticas; para cargas Python/ML, el soporte GPU y el escalado serverless simplifican la infraestructura.
