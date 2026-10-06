---
title: "Vibecoding isn't as fun as writing code by hand — The Autodidacts"
source_url: "https://www.autodidacts.io/vibecoding-isnt-as-fun-as-writing-code-by-hand/"
date: 2026-10-06
---

# Vibecoding isn't as fun as writing code by hand — The Autodidacts

Source: https://www.autodidacts.io/vibecoding-isnt-as-fun-as-writing-code-by-hand/

I like building things: it makes me happy. Learning and discovering things is a close second, but building is more satisfactory.

Since I’m not that good at actually, you know, _building_ things, the thrill of “building”, in my case, has mostly come from writing software. Software is one of the easiest ways to create something satisfyingly useful out of nothing.

For a long time I’ve known, at some level, how much joy building gives me. [1] But it really sunk in while working on two recent hobby software projects. They were both dumb little Python scrapers that I cobbled together, that did something useful that I’d wanted for a long time. ([Link](https://salez.ca/?ref=autodidacts.io), [link](https://www.curiositry.com/free-silver-price-api/?ref=autodidacts.io).) They were pretty basic, but gave me so much irrational pleasure. It was the most fun I’d had programming in years. [2]

Then, _[cue Jaws theme song]_ AI came along.

Like pretty much everyone else, I’ve been cautiously experimenting with AI-assisted coding. We are past the point where we can easily dismiss AI as “stupid” (though it is), or “doesn’t actually make me more productive”. So, in classic motte and bailey fashion, I am retreating, while pretending not to: AI coding is _less fun._

This seems counter-intuitive, because vibecoding is _absolutely thrilling …_ AT FIRST.

Refactoring vibecoded software? Not thrilling.

I’m not going to claim, as some do, that vibecoding doesn’t give the thrill of actually building something. Because it does, partly.

I think that one of the things that’s driving the adoption of vibecoding is that it **frontloads the fun** , at both the project- and career level.

![AI Vibecoding vs Coding By Hand Thrill/Fun/Learning Curve Graph](https://www.autodidacts.io/content/images/2026/08/ai-vibecoding-vs-coding-by-hand-thrill-learning-fun-curve.png) The Vibecoding Thrill Curve

If I have an idea, I can usually get a working prototype _very_ quickly, with very little effort. Instant dopamine!

Similarly, someone with no coding experience can “code” an app, and it will probably work. Instant dopamine!

I have a personal policy against frontloading the fun. So, I don’t like this, just like I don’t like getting paid for work I haven’t done, going into debt, and arrangements where someone else does my work today in trade for me doing their work tomorrow.

I posit that there are several distinct sources of thrill/satisfaction when building something:

1. The thrill of the idea
2. The thrill of making the idea real
3. The satisfaction of hard-won accomplishment
4. The satisfaction of a job well done
5. The thrill of learning
6. The satisfaction making something that solves a problem you have

Vibecoding, in general, can give you 1, 2, and 6. But 3, 4, and 5 are not natural consequence of vibecoding.

In tenuous defense of vibecoding:

I can, and have, built things with AI that I either never could have, or never would have, built otherwise. Mostly, it’s cases where it would not be worth me spending weeks building it by hand, but if I can build it in minutes or days, it is worth it.

- I one-shotted a _has-this-already-been-submitted-to-hackernews_ bookmarklet ([HN?](<javascript:void%20function(){javascript:(function(){%22use%20strict%22;const%20a=10,b=a=%3E{try{const%20b=new%20URL(a);return%20b.search=%22%22,b.hash=%22%22,b.toString()}catch(b){return%20a}},c=a=%3E{if(!a||0===a.hits.length)return%20null;let%20b=a.hits[0],c=-1;a.hits.forEach(a=%3E{a.points%3Ec%26%26(c=a.points,b=a)});const%20d=a.hits.length,e=new%20Date(b.created_at).toLocaleDateString(),f=document.createElement(%22span%22);return%20f.style.cssText=%22font-size:0.75em;%20color:%23ff6600;%20margin-left:6px;%20font-weight:bold;%20white-space:nowrap;%22,f.innerHTML=`HN:%20${b.points}pts%20|%20${b.num_comments}c%20|%20${d}x%20|%20${e}`,f},d=async%20a=%3E{const%20c=b(a),d=`https://hn.algolia.com/api/v1/search%3Ftags=story%26restrictSearchableAttributes=url%26query=${encodeURIComponent(c)}`;try{const%20a=await%20fetch(d);if(!a.ok)throw%20new%20Error(%22Network%20response%20was%20not%20ok%22);return%20await%20a.json()}catch(a){return%20console.warn(`HN%20Fetch%20failed%20for%20${c}:`,a),null}},e=Array.from(document.querySelectorAll(%22a%22)),f=e.filter(b=%3Eb.href%26%26(b.href.startsWith(%22http://%22)||b.href.startsWith(%22https://%22))),g=new%20Map;f.forEach(a=%3E{const%20c=b(a.href);g.has(c)||g.set(c,a)});const%20h=Array.from(g.entries());let%20i=0;const%20j=()=%3E{if(!(i%3E=h.length)){const%20b=h.slice(i,i+a);i+=a;const%20e=b.map(([a,b])=%3Ed(a).then(a=%3E({linkElement:b,data:a})));Promise.all(e).then(a=%3E{a.forEach(({linkElement:a,data:b})=%3E{const%20d=c(b);d%26%26a.appendChild(d)}),setTimeout(j,200)})}};j()})()}();>)), based on Taylor Troesh’s [Discuss on HN snippet](https://taylor.town/hn-discuss?ref=autodidacts.io). It gave me significant satisfaction, solved a problem I had, I use it regularly on my Wallabag favourites page.

- In very little time, I vibecoded “Party Market”, a prediction market simulator party game to go along with a flash lecture on prediction markets, and ran a market on “how long will I drone on for”, live, during my lecture. It turned a dry and boring lecture into grade-A entertainment. The code was garbage and it was full of bugs, but I never could have done it writing it by hand in that amount of time. It wasn’t a choice between doing it with AI and doing it by hand: it was a choice between doing it with AI _and not doing it at all._

- When a fire chief I know was going to invest way too much money in an “AI appliance” that didn’t even say which Nvidia card it had, or what model/generation of Xeon it was, I vibecoded _with free plan Lumo_ , in two afternoon sessions, a functional Pyronear based Wildfire Early Warning System that ran in realtime on a live feed on my laptop, and was able to detect the first frame of smoke on the ignition footage I fed it.

- I built a browser-based Kobo database migration assistant ([link](https://www.curiositry.com/kobo-data-migration-assistant/?ref=autodidacts.io)), so that people unfamiliar with SQLite can [move their books and annotations to a new device](https://www.autodidacts.io/migrate-kobo-ereader-content-books-annotations-to-new-device/).

- When a singing lesson with my vocal coach fell through, I built the realtime pitch training app I’ve always wanted — and have planned to build for about a decade.

In most of these cases, I was immensely pleased with the results, but the process wasn’t _fun_ the way writing my dumb little scrapers was fun. Of course, handwritten software development isn’t always fun. [My first Golang project](https://github.com/TheAutodidacts/InternetTelegraph?ref=autodidacts.io) was, for large sections of time, with a deadline, certified Not Fun™. Fighting the Rust compiler the first time I tried to write, [like, twenty lines of Rust](https://git.sr.ht/~curiositry/lyric-sheet-formatter?ref=autodidacts.io) code was Not Fun™. But it was, in the long run, Type II fun, because it gave me the sense of accomplishment, and the glorious _I did it!_ feeling (And, next time, it would be easier.)

I’ve tried everything from local models running in llama-server, to copy-and-pasting from free, no sign-up services (Phind, Lumo, etc) for one-shot scripts, to full on remote server Clod Masterpiece 200™ all-you-can-eat plan with custom-written auto-approval hooks that were worryingly close to `–dangerously-skip-permissions`, developing algorithmic trading models.

**It’s all the same** : it’s “productive”, but I don’t like the way it makes me feel, and I don’t like the quality of the output. It manages to [make me feel dumb](https://www.autodidacts.io/underrated-reasons-to-dislike-ai/) and superfluous (and, sometimes, dirty for even using it), without earning my respect.

The word “dopamine” made me think: vibecoding is a bit like a series of first dates or one night stands. You don’t develop a relationship with the project: you don’t get the same kind of warm fuzzies, oxytocin, attachment. The problem with a dopamine-only life is that thrills become dull with repetition.

Another way to look at it: vibecoding introduces a layer between you and reality. I am the kind of person that thinks, in general, reality is _more fun_ when experienced first-hand.

Vibecoding is like being an executive of a large company that is barely under your control. You never feel like you _really_ know what’s going on, and there’s always the suspicion of sabotage and loafing. Things appear fully formed, but not quite how you imagined. Sometimes they work, and sometimes they don’t, and there’s nothing you can do about it, other than pouring more money into the black box, and yelling louder. So that’s what you do.

_This essay was outlined in blue ink by candlelight. AI wasn’t even allowed to correct my typos: savour them._

---

1. As a kid, I wanted to be an inventor, which neatly combines building and discovery. Writing and songwriting, my other main activities, are also forms of building that, like software, require mercifully little contact with physical reality and other humans. ↩︎

2. I’d mostly been writing shell scripts, and Bash is not known for being _fun_. ↩︎

#### Sign up for updates

Join the newsletter for curious and thoughtful people.

Subscribe now! \_\_ No Thanks

Great! Check your inbox and click the link to confirm your subscription.

![](//analytics.autodidacts.io/matomo.php?idsite=1)
