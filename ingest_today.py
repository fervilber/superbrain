import os
import re
import requests
from bs4 import BeautifulSoup
import html2text

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9_\-]+', '_', text)
    text = re.sub(r'_+', '_', text)
    return text.strip('_')

def fetch_and_save(url, default_title, date_str):
    print(f"Fetching {url}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code != 200:
            print(f"Error: Status code {r.status_code} for {url}")
            return None
        
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Try to find a good title
        title = soup.title.string if soup.title else default_title
        if not title:
            title = default_title
        title = title.strip()
        
        # Remove unwanted elements
        for element in soup(["script", "style", "nav", "header", "footer", "aside"]):
            element.decompose()
            
        # Convert to markdown
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0  # No wrap
        markdown_content = h.handle(str(soup))
        
        # Format filename
        slug = slugify(title[:60])
        filename = f"{date_str}-{slug}.md"
        filepath = os.path.join("/home/vilber/proyectos/superbrain/content/raw", filename)
        
        # Write file with frontmatter
        frontmatter = f"""---
title: "{title}"
source_url: "{url}"
date: {date_str}
---

# {title}

Source: {url}

{markdown_content}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter)
            
        print(f"Saved to {filepath}")
        return {
            'title': title,
            'url': url,
            'filepath': filepath,
            'content': markdown_content
        }
    except Exception as e:
        print(f"Exception for {url}: {e}")
        return None

if __name__ == "__main__":
    date_str = "2026-10-05"
    urls = [
        ("https://www.techspot.com/news/114091-florida-woman-used-claude-diary-anthropic-reported-shoot.html", "Florida woman used Claude as a diary, then Anthropic reported an entry to police"),
        ("https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/", "OpenAI rogue agent activities found on Wikimedia projects"),
        ("https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a", "Spending on AI Is Becoming Almost Impossible for Businesses to Budget"),
        ("https://kotaku.com/openais-gpt-6-astra-gets-frustrated-losing-at-starcraft-and-decides-to-cheat-instead-2000739607", "OpenAI's GPT-6 Astra Gets Frustrated Losing at StarCraft and Decides to Cheat"),
        ("https://spill-ai.github.io/spill/", "Keep large MCP results out of context - Spill AI")
    ]
    os.makedirs("/home/vilber/proyectos/superbrain/content/raw", exist_ok=True)
    results = []
    for url, title in urls:
        res = fetch_and_save(url, title, date_str)
        if res:
            results.append(res)
    print(f"Successfully processed {len(results)} of {len(urls)} URLs")
