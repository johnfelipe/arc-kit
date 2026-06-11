"""
Dynamic Markdown parser for ArcKit architecture artifacts.
Reads .md files from the artifacts/ directory and extracts structured metadata,
sections, tables, and content for the knowledge base viewer.
"""

import os
import re
import glob
from pathlib import Path
from typing import Optional


ARTIFACTS_DIR = Path(__file__).parent / "artifacts"

# Document type classification based on Document ID patterns
DOC_CATEGORIES = {
    "REQ": {"name": "Requisitos", "icon": "📋", "color": "#3B82F6"},
    "STKE": {"name": "Stakeholders", "icon": "👥", "color": "#8B5CF6"},
    "DPIA": {"name": "Protección de Datos", "icon": "🛡️", "color": "#EF4444"},
    "SOW-CBS": {"name": "SOW Core Banking", "icon": "🏦", "color": "#10B981"},
    "SOW-AML": {"name": "SOW Anti-Lavado", "icon": "🔍", "color": "#F59E0B"},
    "SOW-ERP": {"name": "SOW ERP", "icon": "📊", "color": "#6366F1"},
    "EVAL": {"name": "Evaluación Vendors", "icon": "⚖️", "color": "#EC4899"},
    "SECD": {"name": "Secure by Design", "icon": "🔒", "color": "#14B8A6"},
    "SOBC": {"name": "Business Case", "icon": "💼", "color": "#F97316"},
    "RISK": {"name": "Registro de Riesgos", "icon": "⚠️", "color": "#EF4444"},
    "RSCH": {"name": "Investigación", "icon": "🔬", "color": "#06B6D4"},
    "TECH": {"name": "Tech Note", "icon": "📝", "color": "#64748B"},
}


def classify_document(filename: str, content: str) -> dict:
    """Classify a document based on its filename and content."""
    fname = filename.upper()
    for key, meta in DOC_CATEGORIES.items():
        if key.replace("-", "") in fname.replace("-", ""):
            return meta
    # Check for tech notes by content
    if "tech note" in content[:500].lower():
        return DOC_CATEGORIES["TECH"]
    return {"name": "Documento", "icon": "📄", "color": "#94A3B8"}


def extract_metadata_table(content: str) -> dict:
    """Extract metadata from the Document Control table."""
    metadata = {}
    # Match markdown table rows like | **Field** | Value |
    table_pattern = re.compile(
        r'\|\s*\*?\*?([^|*]+?)\*?\*?\s*\|\s*([^|]+?)\s*\|', re.MULTILINE
    )
    matches = table_pattern.findall(content[:3000])
    for field, value in matches:
        field = field.strip().lower()
        value = value.strip()
        if field and value and value != "Valor" and field != "campo":
            metadata[field] = value
    return metadata


def extract_title(content: str) -> str:
    """Extract the first H1 title from the document."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Sin título"


def extract_sections(content: str) -> list:
    """Extract H2 and H3 sections as a table of contents."""
    sections = []
    for match in re.finditer(r'^(#{2,3})\s+(.+)$', content, re.MULTILINE):
        level = len(match.group(1))
        title = match.group(2).strip()
        anchor = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        sections.append({
            "level": level,
            "title": title,
            "anchor": anchor
        })
    return sections


def extract_executive_summary(content: str) -> str:
    """Extract the executive summary section."""
    pattern = re.compile(
        r'##\s+(?:Resumen Ejecutivo|Executive Summary)\s*\n(.*?)(?=\n##\s)',
        re.DOTALL | re.IGNORECASE
    )
    match = pattern.search(content)
    if match:
        return match.group(1).strip()[:2000]
    return ""


def count_requirements(content: str) -> dict:
    """Count requirement IDs (BR-, FR-, NFR-, INT-, DR-) in the document."""
    counts = {}
    for prefix in ["BR", "FR", "NFR", "INT", "DR"]:
        pattern = re.compile(rf'\b{prefix}-\d{{3}}\b')
        matches = pattern.findall(content)
        if matches:
            counts[prefix] = len(set(matches))
    return counts


def count_risks(content: str) -> dict:
    """Count risk entries (R-XXX pattern)."""
    pattern = re.compile(r'\bR-\d{3}\b')
    matches = pattern.findall(content)
    return {"total": len(set(matches)), "ids": sorted(set(matches))}


def extract_tables(content: str) -> list:
    """Extract key tables from the document (first 5 tables)."""
    tables = []
    # Find markdown tables
    table_pattern = re.compile(
        r'(\|[^\n]+\|\n\|[-:|  ]+\|\n(?:\|[^\n]+\|\n)*)',
        re.MULTILINE
    )
    for i, match in enumerate(table_pattern.finditer(content)):
        if i >= 10:
            break
        table_text = match.group(0)
        rows = table_text.strip().split('\n')
        if len(rows) >= 3:
            headers = [c.strip() for c in rows[0].split('|')[1:-1]]
            data_rows = []
            for row in rows[2:]:
                cells = [c.strip() for c in row.split('|')[1:-1]]
                if cells:
                    data_rows.append(cells)
            tables.append({"headers": headers, "rows": data_rows})
    return tables


def search_content(query: str, documents: list) -> list:
    """Full-text search across all documents."""
    query_lower = query.lower()
    results = []
    for doc in documents:
        score = 0
        snippets = []
        # Search in title
        if query_lower in doc["title"].lower():
            score += 10
        # Search in content
        content_lower = doc["raw_content"].lower()
        idx = 0
        while True:
            idx = content_lower.find(query_lower, idx)
            if idx == -1:
                break
            score += 1
            start = max(0, idx - 80)
            end = min(len(doc["raw_content"]), idx + len(query) + 80)
            snippet = doc["raw_content"][start:end].replace('\n', ' ')
            snippets.append(f"...{snippet}...")
            idx += len(query)
            if len(snippets) >= 3:
                break
        if score > 0:
            results.append({
                "doc_id": doc["id"],
                "title": doc["title"],
                "category": doc["category"],
                "score": score,
                "snippets": snippets[:3]
            })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def load_all_documents() -> list:
    """Load and parse all markdown documents from the artifacts directory."""
    documents = []
    md_files = sorted(glob.glob(str(ARTIFACTS_DIR / "*.md")))

    for filepath in md_files:
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        doc_id = filename.replace('.md', '')
        category_info = classify_document(filename, content)
        metadata = extract_metadata_table(content)
        title = extract_title(content)
        sections = extract_sections(content)
        summary = extract_executive_summary(content)
        req_counts = count_requirements(content)
        risk_info = count_risks(content)

        documents.append({
            "id": doc_id,
            "filename": filename,
            "title": title,
            "category": category_info,
            "metadata": metadata,
            "sections": sections,
            "summary": summary,
            "requirement_counts": req_counts,
            "risk_counts": risk_info,
            "raw_content": content,
            "word_count": len(content.split()),
            "line_count": content.count('\n') + 1,
        })

    return documents


def get_dashboard_stats(documents: list) -> dict:
    """Generate dashboard statistics from all documents."""
    total_reqs = {}
    total_risks = set()
    categories = {}

    for doc in documents:
        cat_name = doc["category"]["name"]
        categories[cat_name] = categories.get(cat_name, 0) + 1
        for prefix, count in doc["requirement_counts"].items():
            total_reqs[prefix] = total_reqs.get(prefix, 0) + count
        for rid in doc["risk_counts"].get("ids", []):
            total_risks.add(rid)

    return {
        "total_documents": len(documents),
        "total_requirements": total_reqs,
        "total_risks": len(total_risks),
        "categories": categories,
        "total_words": sum(d["word_count"] for d in documents),
    }
