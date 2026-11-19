---
title: "A More Predictable Release Cycle for MCP"
source: "https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/"
date: 2026-11-11
captured: 2026-11-19
---

# A More Predictable Release Cycle for MCP

Den Delimarsky, David Soria Parra — Nov 11, 2026, 6 min read.

We're changing how we plan MCP releases. Luca Chang will join Den Delimarsky and David Soria Parra as a release manager for the next specification cycle.

We've spent a lot of time over the past two years talking about ways to improve MCP, add new features and capabilities, and get on a more predictable release cadence. Clearly, there has been no shortage of ideas both from the maintainer and broader developer community. Getting those ideas reviewed, implemented, tested, and into a release is a whole other part of the job, and we want to make that specific part easier to follow for our community.

For folks working on proposals, that means knowing when reviews will happen and how much time there is to make adjustments. SDK maintainers also need to know when the spec will stop changing - both client and server developers use our developer toolchain as a starting point to try new MCP capabilities out and share feedback. To make this process easier, we're setting up a more consistent timeline for upcoming spec changes so that you don't have to piece a schedule together from meeting notes and GitHub threads.

The Core Maintainers worked through these questions together at MCPCon Europe, and Kurtis Van Gent recently wrote up the process in SEP-3398: Release Cycle Updates - this is our de facto release guidance moving forward.

As a result of this work, we're moving MCP specification releases to a regular six-month schedule.

## Two releases a year

We'll generally publish specification releases on the last Tuesday of March and September. Alongside each release date, we'll share the proposal deadlines and SDK beta dates, so you can work backward from them when planning your own implementation and testing.

For the next release, we're targeting March 30, 2027 - expect MCP version `2027-03-30` to land then.

To keep that schedule predictable, a proposal that isn't ready will move to a later release rather than delay the whole spec. Its authors can keep working on it without having to rush, and everyone else can continue preparing for the release they planned around.

Note: This changes how we prepare a release, not MCP messages or version negotiation, so there's nothing you need to change in an existing client or server because of this announcement. Specification versions will continue to use dates.

## Introducing the Release Manager role

Preparing a specification release involves proposal authors, Working Groups, and the maintainers of several SDKs, each with their own work to finish. We need people who can keep track of that work across the project, spot when one team is waiting on another, and help resolve problems before a deadline. That's the job we're formalizing with the Release Manager role.

We'll be working with proposal authors, Working Groups, and SDK maintainers to land each release on the schedule above.
