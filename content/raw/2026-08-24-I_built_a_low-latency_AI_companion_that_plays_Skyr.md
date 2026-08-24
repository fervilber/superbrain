# I built a low-latency AI companion that plays Skyrim with me

URL: https://pantel.is/projects/ai-gaming-companion/

Score: 311

---

Meet Varkos, a somewhat good boy
I Built an AI Companion That Actually Plays With You
A real-time intelligent gaming companion that actually plays alongside you. World agency, local inference, persistent plans, and an AI character designed to create a striking emotional experience.
(Currently running in Skyrim, but by design pluggable anywhere, standalone too)
See it in action.
A short overview of Varkos playing, planning and acting inside Skyrim.
:: Contents ::
The goal
Complex commands
Combat
Personality evolution
Dog in and out of the game - Void mode
How it is built
A final word
The goal
Simple: Let's build a super-charged next-level gaming companion that actually feels good.
There are already multiple frameworks that let LLMs control NPC dialogue. They are fantastic for role-playing and staying in character, but they have two recurring problems: weak world agency and latency. Good at talking but far less reliable at performing actions and terrible at complex instruction sets. You may have also noticed how popular AI NPC demos often cut between the player speaking and the AI replying, trying to mask latency. Can we do better?
I wanted a companion that:
Useful and instant.
It should fight, fetch, loot, inspect, carry and give items etc etc, follow complex multi-step instructions without feeling buggy or experimental. This matters especially in VR, where navigating menus is cumbersome and immersion-breaking.
it needs to be FAST fast, not just fast
Alive and present.
It should have a fun, endearing personality, not canned robotic pre-written responses. Remember shared experiences and change over time. The microphone stays active while a session is running: you do not summon Varkos through a dialogue menu, you talk to him.
When immersion kicks in, it should feel like you are not playing alone.
Local and private wherever practical.
The elephant in the room is that cloud LLM calls can get quite pricy (especially with multi-thousand-token LLM calls) and the added latency can be an experience killer. And why turn a private single-player game into a metered and surveilled experience? Let's try to give as much control to the user as possible (bonus it's a fun technical challenge).
Basically: a single-player game where you are not playing alone.
Complex commands
Varkos can handle commands that extend beyond one immediate action. Plans can wait for events, preserve targets between steps, monitor progress and repair or stop when world state changes. Nothing is pre-scripted.
Let's see some examples
Varkos receives a conditional instruction involving the next arrow. He registers the future trigger instead of acting immediately, waits for the correlated projectile impact and then continues the plan.
Long-form multi-step command
âI want you to wait here and Iâm gonna go over there. Once you see the signal, the signal is going to be an arrow I fire up in the sky, I want you to pick up this potion and come and bring it to me. Okay?â
Your browser does not support embedded video.
A deferred command follows a real projectile event in Skyrim.
Item search
Varkos can search the grounded world state for a requested item, identify where it is and respond using what is actually present in the game.
âDo you see the ceremonial sword anywhere?â
Varkos picks up a different sword and brings it to us. We tell him thatâs not the one, then he offers to be on the lookout.
Your browser does not support embedded video.
Finding an item through game state rather than inventing an answer.
Hide-and-seek
Hide-and-seek is not a single API call. It becomes a persistent goal with movement, waiting, monitoring and completion conditions.
âLetâs play hide-and-seek again. You wait here and Iâm gonna go hide, then count to ten and come and try to find me.â
Your browser does not support embedded video.
A game represented as a persistent plan rather than a line of dialogue.
Loot this chest and give me the potion
This combines a grounded container, a filtered loot step and an inventory transfer. Each physical result advances the next part of the plan.
Your browser does not support embedded video.
Loot, select and transfer while preserving the requested item.
Pick up all the items
âPick up all the items and give them to meâ becomes a bounded collection plan over real references. Varkos gathers them, returns and transfers them without pretending that one magical action means âall.â
Your browser does not support embedded video.
A collection plan operating on grounded world objects.
Combat
Varkos receives grounded events from the game, can warn the player through a fast reflex path and uses native body control to act. Instruction plans can strategize (e.g. attack this, then retreat, etc.), and his emotional state can affect how and if he chooses to fight.
Your browser does not support embedded video.
Combat footage 1: dungeon combat.
Your browser does not support embedded video.
Combat footage 2: perception, warning and physical action on the latency-sensitive path.
Personality evolution
Varkos is fully customizable. He does not have to be a demon dog, and the runtime does not have to control only a single character. What systems are applied and what they do, is up to open configuration.
One part of my current build still fully depends on big model/cloud LLM calls: slow personality evolution. This work happens away from the real-time action path. As the player and Varkos travel together, important interactions become evidence for gradual changes to his personality.
My demo Varkos begins as a demon reincarnated as a dog. He considers his canine instincts humiliating, his dog body a prison, and is mistrustful, proud and sarcastic. Through shared experiences he can become more and more domesticated, grow attached to the player and starts enjoying being a dog. Eventually he starts bringing over toys because he wants to play, running off to chase things and seeking affirmation from the player.
Only the starting character traits are authored. The system changes both his explicit traits and his emotional homeostasis. How easily he becomes irritated, frightened, affectionate or playful, etc etc. He can overwrite parts of his vocabulary and code. Changes are versioned and reversible.
I could make it more bounded, but I think there's something fun about some open world clankiness, so how he evolves is up in the air.
Your browser does not support embedded video.
The demon slowly discovers that being a pup is not a bad life.
(And he has learnt to love cabbage...)
Dog in and out of the game - Void mode
My plan is to make this system a gaming companion that can follow you across multiple different games, not just Skyrim (Skyrim felt like a good starting point due to its massive modding community, VR support and big open world).
For this reason he exists outside the game too. When the game closes, he enters âvoid modeâ and cannot see or feel anything. How he responds to that depends on his personality evolution.
Being mean to Varkos results in some pretty grim attitudes.
WTFâ¦ SHUT IT DOWN!
Your browser does not support embedded video.
Speech-only contact after the game world and his body are gone. (Needs sound.)
This state also works as an in-between for different games. One moment Varkos could be fighting a dragon, then the world goes dark, then he appears beside you in Microsoft Flight Simulator. Maybe he would be shocked, need time to understand the new world and slowly learn what its machines and rules mean, or maybe he knows about it already and overjoyed tries to chase the sun.
Let's talk technology now
Unfortunately I am bitter-lesson pilled. Big model is better. If we wanted a perfectly intelligent system then letting a council of hyper-intelligent LLMs control impulses, sensory processing, thinking and acting at sufficient refresh rate would be best.
In some early experiments this worked insanely well, unfortunately today it is too slow and too expensive. I do believe this w
