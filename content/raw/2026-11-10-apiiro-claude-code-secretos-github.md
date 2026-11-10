---
title: 'Captura: Apiiro — el "Don''t Ask Again" de Claude Code expone 1.122 ficheros con secretos en GitHub'
source: "https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html"
date: 2026-11-07
captured: 2026-11-10T20:20:00+01:00
---

# Claude Code's "Don't Ask Again" File Exposes Passwords and Keys in 1,122 Public Copies on GitHub

The Hacker News · 7 de noviembre de 2026 · investigación de Apiiro

## Hallazgos (verbatim)

> Common secret scanners miss many of these files. The researchers ran gitleaks and TruffleHog over every copy, without the tools' verification step. Of the 1,122 files with a secret, gitleaks flagged 564 and TruffleHog 643, and neither flagged 215.
>
> Most misses are passwords typed inside commands. Scanners look for known key formats, and a password after `PGPASSWORD=`, `sshpass -p`, or `mysql -p` looks like an ordinary word in an ordinary command line.
>
> Copies that never reach GitHub still matter, the researchers say. The file is plain JSON in the project folder, and it can also be left inside an npm package, a Docker image, a zip archive, or a synced folder.
>
> Malware has previously looked for secrets on developer machines. In September 2025, the Shai-Hulud worm ran the TruffleHog secret scanner over infected computers, and the scanner flagged more than half of the files as secret.
>
> ### Earlier Reports
>
> Claude Code users have reported this behavior before. An earlier bug report, filed on August 11, 2025, said approved commands with API keys and tokens were being stored word for word in settings.local.json.
>
> An automated bot closed that report as "not planned" on January 3, after 60 days without activity. As of today, the four related reports the researchers cite have all been closed by the same bot, the most recent yesterday. None got a reply from Anthropic, they say.

## Detalle del vector (DEV Community / Gabriel Anhaia, 8 nov 2026)

> That approval doesn't disappear. Claude Code saves it as an `allow` rule in `.claude/settings.local.json`, and an August 2025 bug report says commands with credentials are "stored as is with plain text credentials" in that file. Security firm Apiiro went looking for those files on public GitHub. As The Hacker News reported on November 7, it checked 104,185 copies in 103,617 public repositories and found 1,122 copies holding at least one secret, 1,379 distinct secrets in all.
>
> Claude Code's permissions docs say a Bash approval saved with "Yes, and don't ask again" lasts "permanently per repository and command". The rule goes into `.claude/settings.local.json` at the root of the git repository, and it applies to future sessions anywhere in that repo, worktrees included.
>
> According to the report, the affected files belong to 63 organizations, "mostly software companies of all sizes". Deleting the current file isn't the end of it. **Older versions in git history held 734 more secrets across 509 repositories, and 211 forks of 74 repositories carry the same secrets. Counting shared settings, history and saved agent chat logs, the total is 2,539 secrets across 1,994 repositories**, the figure GBHackers leads with.

## Cobertura de Ars Technica (9 nov 2026)

> Apiiro's researchers found over 100,000 cases where Claude Code's local settings file had been uploaded to a public GitHub repository. Of these, only about 1,100 from 63 different organizations contained secrets such as public API tokens, database passwords, or private keys. **Even after these files are discovered and removed from a repository, the secrets can persist in forks of the original project if a GitHub user isn't careful.**
>
> The leak stems from the way Claude Code handles user approval for automated shell commands. When a user chooses the "Yes, and don't ask again" option to approve running a command, that choice gets stored as part of a rule in the local ".claude/settings.local.json" file on the user's computer. That rule is sometimes coded as a pattern, but the command itself is often written to that settings file as is, including any sensitive information that may be embedded within it.

## Extracto del briefing semanal (aiagentstore.ai, semana del 9 nov 2026)

> **AI coding agents expose a growing secret-management problem.** What changed: A November 8 technology briefing cited research from AppOmni showing that Claude Code's "Don't Ask Again" behavior contributed to more than 1,100 public GitHub files containing live passwords and API keys. The same briefing describes vendors responding with tighter controls for agent access, including governed software-development workflows and narrower, auditable permissions.
>
> Why it matters: Coding agents can accelerate delivery while quietly expanding the number of systems that can read, copy, commit, or transmit credentials. Engineering leaders should treat an agent like an untrusted contractor with powerful tools: limit its permissions, isolate secrets, scan outputs before commits, and maintain detailed logs.
>
> Try/watch: Disable broad approval bypasses, rotate exposed credentials, and require secret scanning in every repository and pull-request path used by an AI coding tool.
