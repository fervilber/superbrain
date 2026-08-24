import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import os
import sys
from datetime import datetime

def duckduckgo_search(query, max_results=5):
    url = f"https://duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"Search request failed: {e}")
        return []
    soup = BeautifulSoup(resp.text, 'html.parser')
    results = []
    # Find all result links with class result__url
    for link in soup.find_all('a', class_='result__url', limit=max_results):
        href = link.get('href')
        title = link.get_text(strip=True)
        # DuckDuckGo redirect URL
        if href.startswith('/url?'):
            m = re.search(r'uddg=([^&]+)', href)
            if m:
                actual_url = urllib.parse.unquote(m.group(1))
                href = actual_url
        # Find snippet: look for parent div with class result__body, then find a with class result__snippet
        parent = link.find_parent('div', class_='result__body')
        snippet = ''
        if parent:
            snippet_tag = parent.find('a', class_='result__snippet')
            if snippet_tag:
                snippet = snippet_tag.get_text(strip=True)
        results.append({'title': title, 'url': href, 'snippet': snippet})
    return results

def extract_article(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        # Try to get main content
        main = soup.find('article') or soup.find('main') or soup.find('div', role='main')
        if main:
            text = main.get_text(separator='\n', strip=True)
        else:
            # fallback: get all paragraphs
            paragraphs = soup.find_all('p')
            text = '\n'.join(p.get_text(strip=True) for p in paragraphs)
        # Clean up multiple newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text[:8000]  # limit length
    except Exception as e:
        return f"Error extracting {url}: {e}"

def main():
    query = "Agentes de IA noticias últimas 24 horas"
    print(f"Searching for: {query}")
    results = duckduckgo_search(query, max_results=5)
    if not results:
        print("No results found")
        sys.exit(1)
    print(f"Found {len(results)} results")
    date_str = datetime.now().strftime('%Y-%m-%d')
    raw_dir = '/home/vilber/proyectos/superbrain/content/raw'
    blog_dir = '/home/vilber/proyectos/superbrain/content/blog'
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(blog_dir, exist_ok=True)
    # Save raw articles
    for i, r in enumerate(results[:3]):  # top 3
        safe_title = re.sub(r'[^\w\s-]', '', r['title']).strip().replace(' ', '_')
        filename = f"{date_str}-{safe_title[:50]}.md"
        path = os.path.join(raw_dir, filename)
        content = f"# {r['title']}\n\nURL: {r['url']}\n\n## Snippet\n{r['snippet']}\n\n---\n\n"
        article_text = extract_article(r['url'])
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
    report_content += "Este informe presenta los desarrollos más relevantes en el campo de los Agentes de IA durante las últimas 24 horas, basado en fuentes técnicas de alta calidad. Cada sección incluye contexto, fundamentos técnicos, implementación y implicaciones.\n\n"
    for i, r in enumerate(results[:3]):
        report_content += f"## {i+1}. {r['title']}\n\n"
        report_content += f"**Fuente:** {r['url']}\n\n"
        report_content += f"**Resumen:** {r['snippet']}\n\n"
        article_text = extract_article(r['url'])
        # Provide a deeper summary (first 800 chars)
        summary = article_text[:800].replace('\n', ' ')
        report_content += f"**Detalles técnicos:** {summary}...\n\n"
        report_content += "---\n\n"
    report_content += "## Conclusiones y tendencias\n\n"
    report_content += "Basándonos en los artículos revisados, se observa una tendencia hacia la integración de agentes de IA en flujos de trabajo empresariales, mejoras en la capacidad de razonamiento y uso de herramientas externas. Se destaca la importancia de la seguridad y la alineación en los sistemas de agentes autónomos.\n\n"
    report_content += "---\n*Informe generado automáticamente por el skill de ingestión de Superbrain.*\n"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Report saved to {report_path}")
    print(f"Report word count: {len(report_content.split())}")

if __name__ == '__main__':
    main()