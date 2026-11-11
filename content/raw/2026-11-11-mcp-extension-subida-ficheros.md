---
title: "Exploring File Uploads and Downloads in MCP (extensión io.modelcontextprotocol/files)"
source: "https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/"
date: 2026-11-10
captured: 2026-11-11
---

# Exploring File Uploads and Downloads in MCP

Autores: Den Delimarsky (Lead Maintainer) y Wil St. Charles (Google). 10 nov 2026, 12 min de lectura.

We're working on an extension for moving files between clients and tools in MCP. It's early, and we'd love your help trying it out.

The Model Context Protocol (MCP) started out as a simple way to connect models to tools, and that principle is still very much at its heart. Over the past two years, the things people build with the protocol have become more ambitious. Much more ambitious. Many of those MCP server projects now need to work with files - often driven by increasing agent capabilities and autonomy.

Saving a PDF from a conversation to cloud storage and pulling a CSV into a sandbox have become very common requests from developers adopting MCP. Today, implementing these scenarios would require a bunch of bespoke tool conventions and transfer mechanisms - not something we'd want folks doing over and over.

Because this request kept coming up in customer discussions, we bootstrapped the File Uploads Working Group. We've spent the last month working through what a solution could look like. Thanks to the effort of our community and developers, we now have a rough extension definition, and we'd love for you to poke at it as we start prototyping and trying out how it works in the wild.

## Where the work stands

The work on the extension is still very much an experimental effort - while we have the shape outlined, we're not sure yet that what we started with is what we'll end up with. The best way to find out is, you guessed it - contact with reality.

You might also notice that there's no reference implementation yet - that's because we expect that a lot of the inner workings will, in fact, be quite different once we start integrating our experiment with third-party file services, such as cloud storage, database import/export, and many others that require file input and output.

As with all other extensions, this one will remain optional - there is no work required on either clients or servers if they don't plan to support it (although we hope they really will, given the broad interest in this work). We expect to finalize the extension and have it become stable before the end of the year.

## How it works

Escenarios guía:

- You have a large file in a conversation, and you want to save it to cloud storage.
- You want to pull a big CSV file into a code sandbox, so your agent can analyze the data or build some Python code around it.
- You want to upload a large presentation, or an HTML deck with all of its assets in a ZIP file to a third-party remote server.

In each of these scenarios, the agent needs to know a bunch of things about the file, but the model doesn't need to read every byte or even handle it directly.

## Detalles de protocolo (descripción de la búsqueda)

The extension identifies itself as `io.modelcontextprotocol/files`, and it works with protocol revision `2026-07-28` and later. A server can advertise it in its `server/discover` response, with `upload` if it accepts files out of band and `maxInlineBytes` if it accepts them inline. A client declares it in the `io.modelcontextprotocol/clientCapabilities` metadata of every request that may need it, including `tools/list`, with `upload` if it can upload out of band and `download` if it accepts download targets.

## Contexto relacionado: Filesystem WG (11 nov 2026)

Agent platforms are converging on presenting services to models as filesystems, and Resources already addresses content by URI under a file:// scheme the specification defines as identifying "resources that behave like a filesystem". Currently, Resources carries that surface in the read direction. The WG will produce a single Extensions Track SEP covering write operations, optimistic concurrency control, and the interaction with change notification and caching.
