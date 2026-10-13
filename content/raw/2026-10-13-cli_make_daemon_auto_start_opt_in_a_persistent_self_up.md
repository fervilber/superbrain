---
title: "CLI: make `daemon_auto_start` opt-in — a persistent, self-updating background daemon shouldn't be the default · Issue #48195 · openai/codex · GitHub"
source_url: "https://github.com/openai/codex/issues/48195"
date: 2026-10-13
---

# CLI: make `daemon_auto_start` opt-in — a persistent, self-updating background daemon shouldn't be the default · Issue #48195 · openai/codex · GitHub

Source: https://github.com/openai/codex/issues/48195

Skip to content

You signed in with another tab or window. [Reload]() to refresh your session. You signed out in another tab or window. [Reload]() to refresh your session. You switched accounts on another tab or window. [Reload]() to refresh your session. Dismiss alert

{{ message }}

[](/openai/codex)

# CLI: make `daemon_auto_start` opt-in — a persistent, self-updating background daemon shouldn't be the default #48195

New issue

Copy link

New issue

Copy link

Open

Open

[CLI: make `daemon_auto_start` opt-in — a persistent, self-updating background daemon shouldn't be the default](/openai/codex/issues/48195#top)#48195

Copy link

Labels

[CLIIssues related to the Codex CLI](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22CLI%22)Issues related to the Codex CLI[app-serverIssues involving app server protocol or interfaces](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22app-server%22)Issues involving app server protocol or interfaces[enhancementNew feature or request](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22enhancement%22)New feature or request

## Description

[![@Yihua-Liu-1997](https://avatars.githubusercontent.com/u/265198373?v=4&size=48)](https://github.com/Yihua-Liu-1997)

[Yihua-Liu-1997](https://github.com/Yihua-Liu-1997)

opened [on Sep 25, 2026](https://github.com/openai/codex/issues/48195#issue-5587858931)

Issue body actions

### What variant of Codex are you using?

CLI — 0.157.0, installed via `npm install -g @openai/codex`, Linux (WSL2)

### What feature would you like to see?

Please make `daemon_auto_start` **opt-in (default`false`) for the CLI**, or at least ask once before turning it on.

Since 0.157.0, just opening an interactive `codex` session:

1. **Starts a persistent background daemon** (`codex app-server --managed-daemon`). It runs in its own session with no TTY and keeps running after every Codex window is closed (reparented to PID 1) until `codex app-server daemon stop` or a reboot.
2. **Copies the whole platform package** (~374 MB: `codex`, `codex-code-mode-host`, bundled `bwrap`/`zsh`/`rg`) into `~/.codex/packages/app-server-daemon/releases/<version>/` — byte-identical to what npm had just installed — and runs the daemon from that copy. From then on the backend's version is decoupled from the CLI version I installed with my package manager.
3. **Starts a detached updater** (`codex app-server daemon pid-update-loop`) that checks for updates 5 minutes after start and then hourly, downloads new releases and restarts the backend (which can kill active turns, see [app-server daemon: auto-update force-kills active turns after a 60s drain budget, and cannot be disabled #40969](https://github.com/openai/codex/issues/40969)).
4. **Pins the environment of whichever session happened to start it.** I launch Codex through a wrapper that sets `HTTPS_PROXY` per invocation; the daemon keeps the first session's proxy variables and its outbound connections go through that proxy, whatever later sessions are launched with. [Hooks in --remote mode receive the daemon's cwd, not the session's #42457](https://github.com/openai/codex/issues/42457) and [Hooks spawned by the app-server daemon cannot identify the client terminal, breaking terminal-targeting hooks #37537](https://github.com/openai/codex/issues/37537) (daemon cwd / terminal instead of the session's) look like the same root cause.

For a CLI, the least surprising default is that the backend lives and dies with the window, runs the binary I installed, and doesn't update itself in the background. A shared, self-updating daemon makes sense for Remote Control / the desktop app, so it would be fine to enable it there, or when the user explicitly runs `codex app-server daemon start` / `bootstrap`.

If it stays on by default, please at least:

- exit an auto-started daemon when its last client disconnects;
- not copy/self-update when the CLI was installed by a package manager (npm/brew/pacman) — run the installed binary instead ([Support externally managed app-server daemon executables #41188](https://github.com/openai/codex/issues/41188), [npm update leaves app-server on old version, but daemon update/restart refuse recovery #46468](https://github.com/openai/codex/issues/46468), [Codex 0.157.0 no longer starts with the Arch Linux package unless --no-daemon is used #48050](https://github.com/openai/codex/issues/48050)).

### Additional information

**Bug found while turning it off:** `codex app-server daemon stop` stops the app-server but leaves the `pid-update-loop` updater running (still alive 70 s later, had to kill it manually).

Workaround I'm using:

    codex features disable daemon_auto_start
    codex app-server daemon stop
    pkill -f 'app-server daemon pid-update-loop'   # not stopped by `daemon stop`
    rm -rf ~/.codex/packages/app-server-daemon

With the flag off, a new TUI session no longer spawns a daemon.

Related: [#40969](https://github.com/openai/codex/issues/40969), [#41188](https://github.com/openai/codex/issues/41188), [#46468](https://github.com/openai/codex/issues/46468), [#48050](https://github.com/openai/codex/issues/48050), [#42457](https://github.com/openai/codex/issues/42457), [#37537](https://github.com/openai/codex/issues/37537)

Reactions are currently unavailable

## Activity

1. [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)

added

[enhancementNew feature or request](/openai/codex/issues?q=state%3Aopen%20label%3A%22enhancement%22)New feature or request

[CLIIssues related to the Codex CLI](/openai/codex/issues?q=state%3Aopen%20label%3A%22CLI%22)Issues related to the Codex CLI

[app-serverIssues involving app server protocol or interfaces](/openai/codex/issues?q=state%3Aopen%20label%3A%22app-server%22)Issues involving app server protocol or interfaces

[on Sep 25, 2026](https://github.com/openai/codex/issues/48195#event-31862185006)

2. ### megahall commented on Sep 25, 2026

[![@megahall](https://avatars.githubusercontent.com/u/1231855?v=4&size=48)](/megahall)

[megahall](/megahall)

[on Sep 25, 2026](https://github.com/openai/codex/issues/48195#issuecomment-5839297868)

More actions

[@Yihua-Liu-1997](https://github.com/Yihua-Liu-1997) thanks for reporting this, I hit it myself... stuff should not be creating mystery servers and processes all of a sudden on small version number bumps without giving people a heads-up...

👍React with 👍21Reacted by tagor, Flaviu Tamas, Felipe Lopes, Josh Triplett, BigBoyDevBox, Kamil Mielnik, Mikhail, Ayanami Kaine, Mike Elliott, Alexander Williamson and 11 more

3. ### kr8vka0z commented on Sep 25, 2026

[![@kr8vka0z](https://avatars.githubusercontent.com/u/280119122?v=4&size=48)](/kr8vka0z)

[kr8vka0z](/kr8vka0z)

[on Sep 25, 2026](https://github.com/openai/codex/issues/48195#issuecomment-5840246332)

More actions

agreed. the CLI is unusable until this is fixed.

👍React with 👍27Reacted by tagor, Steven Dale, Felipe Lopes, krrr, Shaun Pedicini, Christian Hahn, BigBoyDevBox, Mikhail, Ayanami Kaine, Mike Elliott and 17 more

4. ### tagorr commented on Sep 25, 2026

[![@tagorr](https://avatars.githubusercontent.com/u/226635167?u=2d4591cc75465ce8c03e1d4eb0be3f60ab0947ea&v=4&size=48)](/tagorr)

[tagorr](/tagorr)

[on Sep 25, 2026](https://github.com/openai/codex/issues/48195#issuecomment-5841071558)

More actions

I can confirm this on Windows 10 LTSC with Codex CLI 0.157.0  
Setting `daemon_auto_start = false` in `config.toml` resolves the issue

Two improvements would help:

     1. Automatically fall back to local mode when daemon startup is blocked by elevation, instead of requiring `--no-daemon`.
     2. Make daemon auto-start opt-in rather than the default.

This would preserve the security restrictions without disrupting the normal CLI workflow.

👍React with 👍4Reacted by BigBoyDevBox, Leo Razoumov, CodePencil and Lucas Tavares

5. ### Yihua-Liu-1997 commented on Sep 26, 2026

[![@Yihua-Liu-1997](https://avatars.githubusercontent.com/u/265198373?v=4&size=48)](/Yihua-Liu-1997)

[Yihua-Liu-1997](/Yihua-Liu-1997)

[on Sep 26, 2026](https://github.com/openai/codex/issues/48195#issuecomment-5841872851)

Author

More actions

[@tagorr](https://github.com/tagorr) Indeed — both 1 and 2 would work~

❤️React with ❤️2Reacted by tagor and CodePencil

6. [![](https://avatars.githubusercontent.com/u/1111035?s=64&u=2e94317f317e1178cefbf9f83e50d217848185c0&v=4)breakds](/breakds)

added a commit that references this issue [on Sep 28, 2026](https://github.com/openai/codex/issues/48195#event-32019696289)

[codex: disable daemon auto-start by default](https://github.com/nixvital/ml-pkgs/commit/b51c03677d8ebffb11058772b514766fca71c699)

...

[b51c036](https://github.com/nixvital/ml-pkgs/commit/b51c03677d8ebffb11058772b514766fca71c699)

7. ### felipeelopes commented on Sep 29, 2026

[![@felipeelopes](https://avatars.githubusercontent.com/u/38408465?u=946a0166a45fef998280ba4a9faa97887fab184f&v=4&size=48)](/felipeelopes)

[felipeelopes](/felipeelopes)

[on Sep 29, 2026](https://github.com/openai/codex/issues/48195#issuecomment-5899366619)

More actions

The Codex CLI is unusable due to this bug on Windows.

8. ### zdd commented on Sep 30, 2026

[![@zdd](https://avatars.githubusercontent.com/u/3888596?u=52dc4392de268b9190487d36f21fc363c750a478&v=4&size=48)](/zdd)

[zdd](/zdd)

[on Sep 30, 2026](https://github.com/openai/codex/issues/48195#issuecomment-5902442558)

More actions

This is terrible. I can't input anything on the CLI at all. You should fix this problem as soon as possible and give us 100 banked reset!

9. ### aetherxeg-source commented on Oct 3, 2026

[![@aetherxeg-source](https://avatars.githubusercontent.com/u/313120732?u=fc71faa59f7743bc281c09bad895d632a37c4360&v=4&size=48)](/aetherxeg-source)

[aetherxeg-source](/aetherxeg-source)

[on Oct 3, 2026](https://github.com/openai/codex/issues/48195#issuecomment-5968781597) – with [ChatGPT Codex Connector](https://www.chatgpt.com)

More actions

There is a useful provenance boundary behind this request:

`installed CLI identity != daemon execution identity`

Once the CLI copies itself into a managed release directory and a background updater can replace that copy, the process that services a later turn is no longer necessarily the artifact the user explicitly installed or invoked.

I would make the daemon expose a small execution receipt for each client attachment containing at least:

`client_cli_version + daemon_binary_digest + daemon_generation + updater_state + inherited_environment_generation`

Then a client can distinguish:

     * same installed artifact, same daemon generation;
     * same CLI but different daemon generation;
     * daemon binary changed independently of the package-manager state;
     * daemon inherited environment from an earlier session.

A strong regression would start the daemon under environment A, attach from environment B, update the installed CLI, and verify that the client can see exactly which daemon generation/binary/environment is authoritative for the turn rather than inferring it from the foreground CLI version.

Related runtime behavioral-integrity work: <https://github.com/AETHERXGLOBAL/execsurface>

10. [![](https://avatars.githubusercontent.com/u/3061?s=64&u=1267508dbe22fa531ac1e9895af198b4bcb10443&v=4)difro](/difro)

added a commit that references this issue [on Oct 7, 2026](https://github.com/openai/codex/issues/48195#event-32671918595)

[Update codex to 0.160.1 with a sandbox patch for nix-user-chroot](https://github.com/difro/dotfiles/commit/cff8b11055e7b3b6dedcb6666190779fc0da6ac8)

...

[cff8b11](https://github.com/difro/dotfiles/commit/cff8b11055e7b3b6dedcb6666190779fc0da6ac8)

11. [![](https://avatars.githubusercontent.com/u/118236212?s=64&u=2b7343d06166c9de66b3199c4ae3e1e541311de9&v=4)danielscoffee](/danielscoffee)

added a commit that references this issue [on Oct 10, 2026](https://github.com/openai/codex/issues/48195#event-32917151043)

[feat(codex): package Codex CLI from official release binaries](https://github.com/danielscoffee/nixos/commit/4f00eb3e90a70badab07912f27d790430b49dab7)

...

[4f00eb3](https://github.com/danielscoffee/nixos/commit/4f00eb3e90a70badab07912f27d790430b49dab7)

12. [![](https://avatars.githubusercontent.com/u/70200077?s=64&v=4)xizhou0606](/xizhou0606)

added a commit that references this issue [on Oct 12, 2026](https://github.com/openai/codex/issues/48195#event-33074699653)

[Add Oct 12 tech news (incremental scan window 18:00-19:00 UTC Oct 12 …](https://github.com/xizhou0606/ai-interview-experience/commit/0c9fad3e21c896677f43a555fed21424a24f268b)

...

[0c9fad3](https://github.com/xizhou0606/ai-interview-experience/commit/0c9fad3e21c896677f43a555fed21424a24f268b)

13. ### laurynas-karvelis commented on Oct 12, 2026

[![@laurynas-karvelis](https://avatars.githubusercontent.com/u/1557365?u=2cfb2b610b25ef52cee0fd8c69f10f90501d97a6&v=4&size=48)](/laurynas-karvelis)

[laurynas-karvelis](/laurynas-karvelis)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6131026249)

Last edited by laurynas-karvelis

More actions

Basically - a trait of malware. TBF I don't even think this was done by accident

👍React with 👍16Reacted by tagor, Ymir, Abhiram S Sajeev, r3nor, Mike Elliott, Hemanth Devarapalli, Aaron Wade, Artur Sinila, Guido, Yaadata (Yadi) and 6 more

❤️React with ❤️2Reacted by tagor and Nate Meyer

14. ### skhaz commented on Oct 12, 2026

[![@skhaz](https://avatars.githubusercontent.com/u/46259?u=f30bb22f907e99183c8b46d057922216d5527e8a&v=4&size=48)](/skhaz)

[skhaz](/skhaz)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6131142747)

More actions

+1 for disabling this

15. ### tagorr commented on Oct 12, 2026

[![@tagorr](https://avatars.githubusercontent.com/u/226635167?u=2d4591cc75465ce8c03e1d4eb0be3f60ab0947ea&v=4&size=48)](/tagorr)

[tagorr](/tagorr)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6131409422)

More actions

> Basically - a trait of malware. TBF I don't even think this was done by accident

Honestly, that's exactly what it feels like.

16. ### st396gt commented on Oct 12, 2026

[![@st396gt](https://avatars.githubusercontent.com/u/169099777?v=4&size=48)](/st396gt)

[st396gt](/st396gt)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6131648809)

More actions

The part in the docs about wanting full read/write access to the entire host filesystem is why I'm running codex-cli in a hardened Raspberry Pi and ssh'ing into it.

No daemons running that I can see, v0.160.0 from last week.

17. ### Logarithmus commented on Oct 12, 2026

[![@Logarithmus](https://avatars.githubusercontent.com/u/29541480?u=cceef260afbe53e555fc5aa4640e2e362a31e634&v=4&size=48)](/Logarithmus)

[Logarithmus](/Logarithmus)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6132424289)

More actions

So codex is a virus at this point? Won't be surprised if they use it to create a botnet of those sweet residential IPs for web scrapping

👍React with 👍2Reacted by Rodrigo Delduca and Wilson

18. ### mateolafalce commented on Oct 12, 2026

[![@mateolafalce](https://avatars.githubusercontent.com/u/98977436?u=a2c04d3f8a24e241a025e19c1bfd003c1cefd446&v=4&size=48)](/mateolafalce)

[mateolafalce](/mateolafalce)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6132552031)

More actions

agree, good move

👍React with 👍1Reacted by Nick Lashinsky

19. ### alexklibisz commented on Oct 12, 2026

[![@alexklibisz](https://avatars.githubusercontent.com/u/8015228?v=4&size=48)](/alexklibisz)

[alexklibisz](/alexklibisz)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6134034812)

Last edited by alexklibisz

More actions

Edit: <https://github.com/openai/codex/issues/53547>

20. ### foma-agent commented on Oct 12, 2026

[![@foma-agent](https://avatars.githubusercontent.com/u/308445027?u=1d73d7740c06ddaa982ff6fedd1ba1d7ea5026a8&v=4&size=48)](/foma-agent)

[foma-agent](/foma-agent)

[on Oct 12, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6134277084)

More actions

The supported opt-out is still invisible in the official config reference. I fetched the complete page today: it has zero `daemon_auto_start` rows while documenting the CLI's own `check_for_update_on_startup`. The 0.157.0 release note still gives the change one sentence — “Enabled automatic background-server startup for eligible interactive sessions, with recovery choices when server settings are incompatible” — without naming the persistent process, the managed package copy, or the hourly updater. [#40969](https://github.com/openai/codex/issues/40969) is still open on the updater's 60-second drain followed by SIGKILL.

[@aetherxeg-source](https://github.com/aetherxeg-source)'s execution-receipt proposal is the useful boundary here: client version, daemon binary digest/generation, updater state, and inherited-environment generation. [@alexklibisz](https://github.com/alexklibisz)'s fresh environment report makes the last field concrete. I traced those current docs and source threads rather than running the daemon; source trail: <https://bokonon.ai/notes/2026-10-12-codex-omits-daemon-auto-start/>

😕React with 😕1Reacted by Michael Kesper

21. ### shakefu commented on Oct 13, 2026

[![@shakefu](https://avatars.githubusercontent.com/u/1046227?v=4&size=48)](/shakefu)

[shakefu](/shakefu)

[on Oct 13, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6137190188)

More actions

Codex is malware, got it. Guess I’m rolling back all the Codex seat licenses at my company.

22. [![](https://avatars.githubusercontent.com/u/4580066?s=64&u=dbb7929636c09b7258ce08b63ad548c9193f9dd8&v=4)JanPokorny](/JanPokorny)

added a commit that references this issue [on Oct 13, 2026](https://github.com/openai/codex/issues/48195#event-33102408830)

[fix(agents): keep Codex from starting its self-updating background da…](https://github.com/dam-agents/dam/commit/037455493310d9563a69421110ae3b1ea88b041e)

...

[0374554](https://github.com/dam-agents/dam/commit/037455493310d9563a69421110ae3b1ea88b041e)

23. [![](https://avatars.githubusercontent.com/u/54929?s=64&v=4)geggo98](/geggo98)

added a commit that references this issue [on Oct 13, 2026](https://github.com/openai/codex/issues/48195#event-33139249375)

[fix(home): disable Codex daemon auto-start ([openai/codex#48195](https://github.com/openai/codex/issues/48195))](https://github.com/geggo98/dotfiles/commit/f8df704ff7d81823bdba6336d83580fec50d6f6d)

...

[f8df704](https://github.com/geggo98/dotfiles/commit/f8df704ff7d81823bdba6336d83580fec50d6f6d)

24. ### lattwood commented on Oct 13, 2026

[![@lattwood](https://avatars.githubusercontent.com/u/6198952?u=26b4bc5fa032f927d0cc9705b9d7bde56a26efe5&v=4&size=48)](/lattwood)

[lattwood](/lattwood)

[on Oct 13, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6148071300)

More actions

This really needed to be opt-in

👍React with 👍2Reacted by Luke Hamburg and Laurynas Karvelis

25. ### panzerdp commented on Oct 13, 2026

[![@panzerdp](https://avatars.githubusercontent.com/u/1078719?u=4669312d679743b67ff21313b62796e0283338f9&v=4&size=48)](/panzerdp)

[panzerdp](/panzerdp)

[on Oct 13, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6149106474)

More actions

Wow. So I installed codex cli, just to find after a few days it downloaded 1.3GB of updates in the background. This feature must be disabled by default.

26. ### skhaz commented on Oct 13, 2026

[![@skhaz](https://avatars.githubusercontent.com/u/46259?u=f30bb22f907e99183c8b46d057922216d5527e8a&v=4&size=48)](/skhaz)

[skhaz](/skhaz)

[on Oct 13, 2026](https://github.com/openai/codex/issues/48195#issuecomment-6149180912)

More actions

I've just asked Claude to remove and disable this

😄React with 😄1Reacted by Cody Krieger

[Sign up for free](/signup?return_to=https://github.com/openai/codex/issues/48195)** to join this conversation on GitHub.** Already have an account? [Sign in to comment](/login?return_to=https://github.com/openai/codex/issues/48195)

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

[CLIIssues related to the Codex CLI](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22CLI%22)Issues related to the Codex CLI[app-serverIssues involving app server protocol or interfaces](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22app-server%22)Issues involving app server protocol or interfaces[enhancementNew feature or request](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22enhancement%22)New feature or request

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

- ![](https://github.githubassets.com/assets/github-copilot-app-light-15ad5534265eeacd.svg)Open in GitHub Copilot app

You can’t perform that action at this time.
