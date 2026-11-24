#!/usr/bin/env python3
"""Build an isolated Quartz preview from explicitly approved documents.

Never copies the source vault wholesale. No source raw/, sessions/ or logs are read.
The approved list is intentionally tiny until a full editorial/security review.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "superbrain/prueba"
HOST = "bolsafer.duckdns.org"
APPROVED = (
    "blog/Informe-2026-11-20.md",
    "blog/Informe-2026-11-23.md",
)
# Fail closed: do not rewrite unknown private paths or replace secrets in place.
FORBIDDEN = (
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{32,}\b"),
    re.compile(r"\]\((?:https?://[^)]*)?/?raw/[^)]*\)"),
    re.compile(r"(?:/home/vilber/|144\.91\.108\.254|fervilber@(?:gmail\.com|pm\.me))"),
)


def reject(text: str, name: str) -> None:
    for pattern in FORBIDDEN:
        if pattern.search(text):
            raise RuntimeError(f"Revisión requerida en {name}: patrón prohibido {pattern.pattern!r}")


def main() -> None:
    target = Path(os.environ.get("SUPERBRAIN_PREVIEW_OUTPUT", str(ROOT / "public" / "prueba"))).resolve()
    if target == ROOT / "public" or ROOT not in target.parents:
        raise RuntimeError("La prueba debe permanecer bajo public/ y no sustituir el sitio actual")
    registry = json.loads((ROOT / "publication-review.json").read_text())
    states = {item["ruta"]: item["estado"] for item in registry["informes"]}
    if len(states) != registry["expected_total"] or set(states) != set(
        subprocess.check_output(["git", "ls-files", "content/blog/*.md"], cwd=ROOT, text=True).splitlines()
    ):
        raise RuntimeError("El registro de revisión no cubre exactamente los informes rastreados")
    if any(states.get("content/" + item) != "aprobacion_preliminar" for item in APPROVED):
        raise RuntimeError("La prueba contiene informes no aprobados preliminarmente")
    with tempfile.TemporaryDirectory(prefix="superbrain-preview-") as tmp:
        stage = Path(tmp)
        for name in ("quartz", "node_modules", ".quartz", "quartz.lock.json", "package.json", "quartz.ts", "tsconfig.json", "globals.d.ts", "index.d.ts"):
            source = ROOT / name
            if source.exists():
                (stage / name).symlink_to(source, target_is_directory=source.is_dir())
        cfg = (ROOT / "quartz.config.default.yaml").read_text()
        old = "baseUrl: fervilber.github.io/superbrain"
        if cfg.count(old) != 1:
            raise RuntimeError("La configuración Quartz cambió: revisar manualmente baseUrl")
        (stage / "quartz.config.default.yaml").write_text(cfg.replace(old, f"baseUrl: {HOST}/{PREFIX}"))
        content = stage / "content"
        content.mkdir()
        links = []
        for item in APPROVED:
            source = ROOT / "content" / item
            if not source.is_file():
                raise RuntimeError(f"Falta el documento aprobado: {item}")
            body = source.read_text()
            reject(body, item)
            dest = content / item
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(body)
            links.append(f"- [{Path(item).stem}](./{item})")
        index = "# Superbrain — prueba de publicación\n\nEsta prueba incluye únicamente dos informes revisados; no es aún el blog completo.\n\n## Informes\n\n" + "\n".join(links) + "\n"
        (content / "index.md").write_text(index)
        output = stage / "public"
        subprocess.run(["npx", "quartz", "build", "-d", "content", "-o", str(output), "-c", "2"], cwd=stage, check=True)
        index_json = json.loads((output / "static/contentIndex.json").read_text())
        expected = {"index", *(item.removesuffix(".md").lower() for item in APPROVED)}
        indexed_notes = {key for key in index_json if key == "index" or key.startswith("blog/") and key != "blog/index"}
        if not expected.issubset(indexed_notes):
            raise RuntimeError(f"Faltan notas aprobadas: {expected - indexed_notes}")
        if any(key.startswith(("raw/", "sessions/", "log")) for key in index_json):
            raise RuntimeError("El índice de búsqueda contiene material interno")
        files = {str(p.relative_to(output)) for p in output.rglob("*") if p.is_file()}
        if any(x.startswith(("raw/", "sessions/", "log")) for x in files):
            raise RuntimeError("La salida contiene material interno")
        text_files = (p for p in output.rglob("*") if p.is_file() and p.suffix in (".html", ".xml", ".json", ".js"))
        for p in text_files:
            reject(p.read_text(errors="replace"), str(p.relative_to(output)))
        if target.exists():
            shutil.rmtree(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(output, target)
        print(f"Prueba construida: {target}; páginas indexadas: {len(index_json)}; archivos: {len(files)}")


if __name__ == "__main__":
    main()
