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
        slug = slugify(title[:50])
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
    date_str = "2026-10-04"
    urls = [
        ("https://github.com/Niko1221/Strata", "Strata: Run Qwen 3.8 Flash Next on RTX 4090"),
        ("https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/", "Default hard budget caps on everything - Simon Willison"),
        ("https://alexeyindeev.substack.com/p/i-stopped-reviewing-my-agents-code", "I stopped reviewing my agents' code. Here's what I do instead"),
        ("https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken", "OpenAI safety leader quits, warning AI company's culture is 'broken'")
    ]
    os.makedirs("/home/vilber/proyectos/superbrain/content/raw", exist_ok=True)
    for url, title in urls:
        fetch_and_save(url, title, date_str)
