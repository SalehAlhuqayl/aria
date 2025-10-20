from __future__ import annotations

import re
import shutil
from pathlib import Path

import markdown

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = PROJECT_ROOT / "docs" / "10-manuscript.md"
FIG_SRC_DIR = PROJECT_ROOT / "data" / "output" / "figures"
OUT_DIR = PROJECT_ROOT / "output" / "paper"
INDEX_HTML = OUT_DIR / "index.html"


def copy_figures(out_dir: Path) -> None:
    figs_out = out_dir / "figures"
    figs_out.mkdir(parents=True, exist_ok=True)
    if FIG_SRC_DIR.exists():
        for p in FIG_SRC_DIR.glob("*.png"):
            shutil.copy2(p, figs_out / p.name)


def rewrite_image_paths(md_text: str) -> str:
    # Replace ../data/output/figures/*.png with figures/*.png
    return re.sub(r"\(\.\./data/output/figures/([^)]+)\)", r"(figures/\1)", md_text)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    md_text = MANUSCRIPT.read_text(encoding="utf-8")
    md_text = rewrite_image_paths(md_text)

    html = markdown.markdown(md_text, extensions=[
        "toc",
        "tables",
        "fenced_code",
        "codehilite",
        "attr_list",
    ])

    # Simple HTML wrapper
    template = f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Used Car Prices in Saudi Arabia - Manuscript</title>
<style>
body {{ font-family: -apple-system, Segoe UI, Roboto, Arial, sans-serif; max-width: 900px; margin: 2rem auto; padding: 0 1rem; }}
h1, h2, h3 {{ margin-top: 1.6rem; }}
table {{ border-collapse: collapse; }}
th, td {{ border: 1px solid #ddd; padding: 6px 8px; }}
img {{ max-width: 100%; height: auto; }}
code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }}
pre code {{ display: block; padding: 8px; }}
</style>
</head>
<body>
{html}
</body>
</html>
"""
    INDEX_HTML.write_text(template, encoding="utf-8")

    copy_figures(OUT_DIR)

    # Create a zip bundle
    shutil.make_archive(str(OUT_DIR), "zip", OUT_DIR)
    print(f"Exported HTML to {INDEX_HTML}")


if __name__ == "__main__":
    main()
