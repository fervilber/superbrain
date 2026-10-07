import requests
import time
import json

now = int(time.time())
day_ago = now - 24 * 3600

queries = ['agent', 'LLM', 'AI', 'DeepSeek', 'OpenAI', 'Anthropic', 'MCP']
results = []

for q in queries:
    url = f"https://hn.algolia.com/api/v1/search_by_date?query={q}&tags=story&numericFilters=created_at_i>{day_ago}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            hits = r.json().get('hits', [])
            for h in hits:
                results.append({
                    'title': h.get('title'),
                    'url': h.get('url') or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                    'points': h.get('points'),
                    'num_comments': h.get('num_comments'),
                    'created_at': h.get('created_at'),
                    'created_at_i': h.get('created_at_i'),
                    'story_id': h.get('objectID'),
                    'query': q
                })
    except Exception as e:
        print(f"Error fetching query {q}: {e}")

deduped = {}
for r in results:
    sid = r['story_id']
    if sid not in deduped or r['points'] > deduped[sid]['points']:
        deduped[sid] = r

sorted_results = sorted(deduped.values(), key=lambda x: x['points'], reverse=True)
print(json.dumps(sorted_results[:20], indent=2))
