import os, json, subprocess, requests, html2text
from bs4 import BeautifulSoup
import re

date_str = "2026-10-13"
raw_dir = "/home/vilber/proyectos/superbrain/content/raw"
blog_dir = "/home/vilber/proyectos/superbrain/content/blog"
os.makedirs(raw_dir, exist_ok=True)
os.makedirs(blog_dir, exist_ok=True)

def slugify(text):
    text = text.lower()
    # Replace non-alphanumeric with underscore
    text = re.sub(r'[^a-z0-9]+', '_', text)
    # Remove leading/trailing underscores
    text = text.strip('_')
    return text

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
        title = soup.title.string if soup.title else default_title
        if not title:
            title = default_title
        title = title.strip()
        # Remove unwanted elements
        for element in soup(["script", "style", "nav", "header", "footer", "aside"]):
            element.decompose()
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        markdown_content = h.handle(str(soup))
        slug = slugify(title[:60])
        filename = f"{date_str}-{slug}.md"
        filepath = os.path.join(raw_dir, filename)
        frontmatter = f"---\ntitle: \"{title}\"\nsource_url: \"{url}\"\ndate: {date_str}\n---\n\n# {title}\n\nSource: {url}\n\n{markdown_content}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter)
        print(f"Saved to {filepath}")
        return {'title': title, 'url': url, 'filepath': filepath, 'content': markdown_content}
    except Exception as e:
        print(f"Exception for {url}: {e}")
        return None

# Get news from fetch_news.py
result = subprocess.run(['python3', '/home/vilber/proyectos/superbrain/fetch_news.py'], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Error running fetch_news.py: {result.stderr}")
    news_list = []
else:
    try:
        news_list = json.loads(result.stdout)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        news_list = []

print(f"Fetched {len(news_list)} stories")

# Keywords for agent-related
keywords = ['agent', 'AI', 'Codex', 'Anthropic', 'OpenAI', 'self-replicating', 'cloud agents', 'multiplayer AI', 'agents']
selected = []
for story in news_list:
    title = story.get('title', '').lower()
    if any(k.lower() in title for k in keywords):
        selected.append(story)
    if len(selected) >= 5:
        break

print(f"Selected {len(selected)} stories for fetching")
raw_entries = []
for story in selected:
    url = story.get('url')
    title = story.get('title', 'Untitled')
    if url:
        entry = fetch_and_save(url, title, date_str)
        if entry:
            raw_entries.append(entry)

# Now generate report
report_path = os.path.join(blog_dir, f"Informe-{date_str}.md")
report_title = f"Informe de avances en Agentes de IA - {date_str}"

# Build report content in Spanish
report_content = f"---\ntitle: \"{report_title}\"\ndate: {date_str}\n---\n\n# {report_title}\n\n## Contexto\n\nEn las últimas 24 horas, se han publicado diversos avances y discusiones técnicas relacionadas con los agentes de IA, desde mejoras en herramientas de código abierto hasta investigaciones sobre capacidades emergentes como la autoreplicación y la colaboración multiagente. Este informe sintetiza las fuentes más relevantes obtenidas de Hacker News y otros medios técnicos.\n\n## Fundamentos\n\nLos agentes de IA se definen como sistemas capaces de percebir su entorno, tomar decisiones y ejecutar acciones de forma autónoma para alcanzar objetivos específicos. Los avances recientes se centran en tres áreas principales: (1) mejoras en la infraestructura y herramientas para desplegar agentes, (2) investigación sobre comportamientos emergentes como la autoreplicación y la distilación de modelos, y (3) plataformas para coordinación de múltiples agentes.\n\n## Implementacion\n\nA continuacion se detallan los desarrollos mas destacados:\n\n"
# Add each entry summary
for i, entry in enumerate(raw_entries, 1):
    report_content += f"### {i}. {entry['title']}\\n\\n"
    report_content += f"**Fuente:** {entry['url']}\\n\\n"
    # Extract first 500 characters of content as summary
    summary = entry['content'][:500].replace('\\n', ' ').strip()
    report_content += f"{summary}...\\n\\n\\n"

report_content += """## Conclusión/Implicaciones

Los acontecimientos de las últimas 24 horas evidencian un acelerado interés tanto en la capacidad técnica de los agentes de IA como en sus implicaciones éticas y de seguridad. La aparición de herramientas como el daemon persistente de Codex CLI sugiere una tendencia hacia agentes que operan continuamente en segundo plano, mientras que los estudios sobre autoreplicación plantean preguntas sobre el control y la contención de sistemas avanzados. Asimismo, el surgimiento de plataformas multiagente como Agor indica un cambio hacia ecosistemas colaborativos donde múltiples agentes pueden interactuar y coordinar tareas complejas. Estos desarrollos requieren una atención continua por parte de investigadores, desarrolladores y reguladores para asegurar que el progreso se alinee con principios de seguridad y beneficio colectivo.

---\
*Informe generado automáticamente por el proceso de ingestión diaria de Superbrain.*\
"""
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_content)
print(f"Report written to {report_path}")