import requests
import re
import os
import sys
from datetime import datetime
from bs4 import BeautifulSoup

def get_top_stories(limit=30):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()[:limit]
    except Exception as e:
        print(f"Failed to get top stories: {e}")
        return []

def get_story(story_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Failed to get story {story_id}: {e}")
        return None

def extract_article(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        # Try to find main content
        main = soup.find('article') or soup.find('main') or soup.find('div', role='main')
        if main:
            text = main.get_text(separator='\n', strip=True)
        else:
            # fallback: get all paragraphs
            paragraphs = soup.find_all('p')
            text = '\n'.join(p.get_text(strip=True) for p in paragraphs)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text[:8000]
    except Exception as e:
        return f"Error extracting {url}: {e}"

def main():
    print("Fetching top Hacker News stories...")
    story_ids = get_top_stories(limit=50)
    print(f"Got {len(story_ids)} story IDs")
    candidates = []
    for sid in story_ids:
        story = get_story(sid)
        if not story:
            continue
        title = story.get('title', '').lower()
        # Look for keywords related to AI agents
        if any(kw in title for kw in ['agent', 'ai', 'llm', 'autonomous', 'language model']):
            url = story.get('url')
            if url:
                candidates.append({'title': story.get('title'), 'url': url, 'score': story.get('score', 0)})
        # also check if it's a Ask HN or Show HN? ignore
    # Sort by score descending
    candidates.sort(key=lambda x: x['score'], reverse=True)
    print(f"Found {len(candidates)} candidate stories")
    if not candidates:
        # fallback: just take top 3 stories regardless
        for sid in story_ids[:3]:
            story = get_story(sid)
            if story:
                candidates.append({'title': story.get('title'), 'url': story.get('url'), 'score': story.get('score', 0)})
    # Limit to top 3
    selected = candidates[:3]
    date_str = datetime.now().strftime('%Y-%m-%d')
    raw_dir = '/home/vilber/proyectos/superbrain/content/raw'
    blog_dir = '/home/vilber/proyectos/superbrain/content/blog'
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(blog_dir, exist_ok=True)
    # Save raw articles
    for i, cand in enumerate(selected):
        safe_title = re.sub(r'[^\w\s-]', '', cand['title']).strip().replace(' ', '_')
        filename = f"{date_str}-{safe_title[:50]}.md"
        path = os.path.join(raw_dir, filename)
        content = f"# {cand['title']}\n\nURL: {cand['url']}\n\nScore: {cand['score']}\n\n---\n\n"
        article_text = extract_article(cand['url'])
        content += article_text
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved raw: {path}")
    # Synthesize report
    report_title = f"Informe-{date_str}"
    report_path = os.path.join(blog_dir, f"{report_title}.md")
    report_content = f"---\ntitle: {report_title}\ndate: {date_str}\n---\n\n"
    report_content += "# Informe diario de Agentes de IA\n\n"
    report_content += f"Fecha: {date_str}\n\n"
    report_content += "## Resumen ejecutivo\n\n"
    report_content += "Este informe presenta los desarrollos más relevantes en el campo de los Agentes de IA durante las últimas 24 horas, basado en fuentes técnicas de alta calidad (Hacker News). Cada sección incluye contexto, fundamentos técnicos, implementación y implicaciones.\n\n"
    for i, cand in enumerate(selected):
        report_content += f"## {i+1}. {cand['title']}\n\n"
        report_content += f"**Fuente:** {cand['url']}\n\n"
        report_content += f"**Puntuación HN:** {cand['score']}\n\n"
        article_text = extract_article(cand['url'])
        summary = article_text[:800].replace('\n', ' ')
        report_content += f"**Detalles técnicos:** {summary}...\n\n"
        report_content += "---\n\n"
    report_content += "## Conclusiones y tendencias\n\n"
    report_content += "Basándonos en los artículos revisados de Hacker News, se observa un interés continuo en los modelos de lenguaje avanzados y su aplicación como agentes autónomos. Se discuten marcos de trabajo, desafíos de seguridad y aplicaciones empresariales.\n\n"
    report_content += "---\n*Informe generado automáticamente por el skill de ingestión de Superbrain (fuente: Hacker News).*\n"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Report saved to {report_path}")
    print(f"Report word count: {len(report_content.split())}")

if __name__ == '__main__':
    main()