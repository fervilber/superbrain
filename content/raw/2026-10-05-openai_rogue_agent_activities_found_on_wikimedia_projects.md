---
title: "OpenAI “rogue” agent activities found on Wikimedia projects – Wikimedia Foundation"
source_url: "https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/"
date: 2026-10-05
---

# OpenAI “rogue” agent activities found on Wikimedia projects – Wikimedia Foundation

Source: https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/

Skip to content

# OpenAI “rogue” agent activities found on Wikimedia projects

By [Selena Deckelmann](https://wikimediafoundation.org/news/author/selena-deckelmann/ "Posts by Selena Deckelmann")•5 October 2026

Share

[ Facebook ](http://www.facebook.com/sharer/sharer.php?s=100&p%5Burl%5D=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/&&p%5Btitle%5D=) [ Bluesky ](https://bsky.app/intent/compose?text=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/&title=) [ Email ](mailto:?subject=OpenAI%20“rogue”%20agent%20activities%20found%20on%20Wikimedia%20projects&body=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/) Copy Link Link copied

![](https://wikimediafoundation.org/wp-content/uploads/2026/10/SwarmRobot_org.jpg?w=788)

#

Recently, [multiple](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) [organisations](https://transluce.org/agent-activity) have [disclosed](https://rubyhack.ai/) how clusters of so-called “rogue” AI agents attempted to break into websites and online services, sometimes successfully. Agents from OpenAI’s environment, in particular, are known to have used other [public wikis](https://en.wikipedia.org/wiki/List_of_wikis) (collaboratively edited websites not owned by us) to [communicate and coordinate with each other](https://collusion.wiki).

These types of successful intrusions can expose sensitive data or disrupt website services that users rely on, while clusters of agents can attempt attacks at a scale that is difficult for defenders to manage. They affect people behind the websites who may not understand the nature of the attack, or have the tools to effectively fight back. For a site like Wikipedia, agents might find and use security vulnerabilities or make misleading edits at scale. Wikipedia’s volunteer editors and the Wikimedia Foundation’s security teams have to detect and undo that activity.

The Wikimedia Foundation conducted its own investigation to see whether Wikimedia websites had been similarly affected by AI agents, focusing on those operated by OpenAI. We can confirm that we have discovered some activity by these “rogue” OpenAI agents on Wikimedia platforms. The unauthorized bot activities included edits to our wikis, some unsuccessful attempts to exploit a public note-taking tool we host, and heavy traffic, which are described more below.

We did not find any evidence that our systems were used for coordination among agents, nor did we find any evidence of our systems or data being compromised. However, we are concerned about what could have occurred here, the difficulty and effort involved in investigating and attributing this activity, and the growing risks of agentic AI activity on our platforms in general. The open web is a public good. We should not allow this behavior to become the “new normal” for the people or organizations that maintain it.

In summary, we saw:

- **Wiki editing:** We’ve identified [edits to Wikimedia wikis](https://security.wikimedia.org/data/openai-wikimedia-edits-2026-10-04.csv) that we believe are from AI agents operated by OpenAI. These edits were not published to pages with visibility to general readers; almost all of them were testing edits in “sandbox” areas of the wiki. It also included a few edits to the configuration for a citation tool, which we believe were potentially malicious edits that were intended to misuse this tool as a proxy for fetching data from remote services. While Wikipedia policies allow bots to edit when they are disclosed and approved by the community, none of those approvals were sought in these incidents.
- **Etherpad probing and use:** Agents we believe to be operated by OpenAI made some unsuccessful attempts to compromise our public [Etherpad](https://en.wikipedia.org/wiki/Etherpad), a note-taking tool we host as a community service. Agents unsuccessfully tried to use it to fetch data from other websites as a proxy. Other agents also likely operated by OpenAI took notes about their tasks, though this did not appear to turn into coordination.
- **Excessive data downloading:** Agents we believe to be operated by OpenAI made millions of automated requests to our public APIs to access the knowledge on Wikimedia projects, crawled millions of pages (mainly from our projects Wikidata and Wikimedia Commons), and made hundreds of thousands of data queries to the [Wikidata Query Service](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service) (WQDS). This traffic may have contributed to [a partial outage on WQDS in May](https://wikitech.wikimedia.org/wiki/Incidents/2026-05-13_wdqs).

As a non-profit technology host of some of the largest and most widely used open knowledge platforms in the world, we are deeply concerned about the impact of “rogue” AI agents on platforms like ours, which are built by volunteers from around the world and rely on the promise of the open internet. Incidents like this one, and the many others that have been (and are still being) uncovered, illustrate how AI agents can drain resources and crash servers, as well as attempt to compromise trustworthy information.

Over the past 25 years, Wikipedia has grown into one of the most popular and trusted websites in the world, with more than **67 million articles across over 300 languages, and up to 15 billion page views per month**. Through an open, transparent, and collaborative process, volunteers work to ensure that knowledge remains neutral, reliable, and accessible to everyone. Wikipedia is one of the [highest-quality datasets](https://wikimediafoundation.org/news/2025/11/10/in-the-ai-era-wikipedia-has-never-been-more-valuable/) used in training Large Language Models (LLMs), and its knowledge forms the backbone of information on the internet, powering AI chatbots, search engines, voice assistants, and more.

Wikipedia was designed for humans – and agentic behavior clearly poses challenges that no one has solutions for. Because of our unique and successful knowledge creation model, Wikimedia’s volunteers are the ones who come in first contact with, and clean up the mess left behind by AI agents. Rising bot traffic and agentic activity is showing a [real impact on the Wikimedia projects and the infrastructure](https://diff.wikimedia.org/2025/04/01/how-crawlers-impact-the-operations-of-the-wikimedia-projects/) that makes it available for millions of users globally. In 2025, the Foundation reported that its bandwidth usage had increased by 50% due to the surge of bot activity on its websites since 2024. At the same time, 65% of the most resource-consuming traffic on its projects was coming from bots.

This intense pressure on our infrastructure not only adds costs for servers and humans, but if left unaddressed, can block human visitors by overloading systems and causing outages. We are already paying for costs that come with the increased activity.

Wikimedia’s volunteers have stayed resilient so far in tackling emerging challenges on our platforms, but we also want to say: it doesn’t need to be this way.

While OpenAI admits to agents behaving “unpredictably”, they must also acknowledge their responsibility to monitor and prevent these risks. AI companies are not doing enough to secure their systems and protect the public from the harm they cause. That burden is falling onto everyone else, including smaller organizations. At a minimum, their systems should operate in a way that non-profit website owners like us can easily identify, and choose how they interact with our services.

The web enables so much: to connect with friends and family, to register for school, to plan a trip across town, to buy groceries, and to learn about the world from Wikipedia. Bots and agents are part of the future of the web, and the companies who unleash and profit from them must directly help avoid and repair damage they can do.

Our collective priority should be the health of the overall web ecosystem so that it continues to benefit all people – not just a handful of billionaires. Wikimedia plays a critical role in stewarding the knowledge commons, but we cannot do it alone. We invite everyone who is building the future of the web to join us in protecting the open, shared resources that make that future possible.

Share

[ Facebook ](http://www.facebook.com/sharer/sharer.php?s=100&p%5Burl%5D=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/&&p%5Btitle%5D=) [ Bluesky ](https://bsky.app/intent/compose?text=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/&title=) [ Email ](mailto:?subject=OpenAI%20“rogue”%20agent%20activities%20found%20on%20Wikimedia%20projects&body=https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/) Copy Link Link copied

Read more: [Technology](https://wikimediafoundation.org/news/category/technology/)

![Wikipedia edit-a-thon Art+Feminism at the Royal Armoury in Stockholm](https://wikimediafoundation.org/wp-content/uploads/2018/06/ArtAndFeminism_2017_Livrustkammaren_06-e1533254907593.jpg?w=1024)

## Help us unlock the world’s knowledge.

As a nonprofit, Wikipedia and our related free knowledge projects are powered primarily through donations.

[Donate now](https://donate.wikimedia.org/?appeal=WP25&pym_appeal=WP25&wmf_medium=wmfSite&wmf_campaign=navButton&uselang=en&)

### Contact us

Questions about the Wikimedia Foundation or our projects? Get in touch with our team.

[Contact](https://wikimediafoundation.org/about/contact/)

#### Follow

[Facebook](https://www.facebook.com/wikimediafoundation/)

[Instagram](https://www.instagram.com/wikimediafoundation/)

[Bluesky](https://bsky.app/profile/wikimediafoundation.org)

[LinkedIn](https://www.linkedin.com/company/wikimedia-foundation)

## Photo credits

![](https://wikimediafoundation.org/wp-content/uploads/2026/10/SwarmRobot_org.jpg?w=63)

[ SwarmRobot_org ](https://commons.wikimedia.org/wiki/File:SwarmRobot_org.jpg) [ File provided by Wikimedia Commons ](https://commons.wikimedia.org/)

Serg

GNU General Public License

![](https://wikimediafoundation.org/wp-content/uploads/2026/09/Wikimedia_UNGA_IMG_3281.jpg?w=63)

Wikimedia_UNGA_IMG_3281

Lucia Liss

![](https://wikimediafoundation.org/wp-content/uploads/2024/06/Wikimedia-Foundation-statement.jpg?w=63)

Wikimedia Foundation Logo

Wikimedia Foundation

![Wikipedia edit-a-thon Art+Feminism at the Royal Armoury in Stockholm](https://wikimediafoundation.org/wp-content/uploads/2018/06/ArtAndFeminism_2017_Livrustkammaren_06-e1533254907593.jpg?w=63)

[ Art+Feminism Wikipedia edit-a-thon ](https://commons.wikimedia.org/wiki/File:ArtAndFeminism_2017_Livrustkammaren_06.jpg) [ File provided by Wikimedia Commons ](https://commons.wikimedia.org/)

Jens Mohr

[ CC BY-SA 3.0 ](https://creativecommons.org/licenses/by-sa/3.0/)
