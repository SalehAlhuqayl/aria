from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"
DATA_OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
LOG_PATH = OUTPUT_DIR / "logs" / "run_experiment.log"
METRICS_PATH = OUTPUT_DIR / "results" / "metrics.json"
SUMMARY_PATH = DATA_OUTPUT_DIR / "execution_summary.txt"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main() -> None:
    DATA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    log_text = read_text(LOG_PATH)
    metrics_text = read_text(METRICS_PATH)

    start_line = next((line for line in log_text.splitlines() if "Starting experiment run" in line), "")
    end_line = next((line for line in log_text.splitlines()[::-1] if "Run complete" in line), "")

    files = []
    if OUTPUT_DIR.exists():
        for p in OUTPUT_DIR.rglob("*"):
            if p.is_file():
                files.append(str(p.relative_to(PROJECT_ROOT)))

    summary_lines = []
    summary_lines.append("Execution Summary")
    summary_lines.append("-----------------")
    summary_lines.append("Parameters: seed=42")
    if start_line:
        summary_lines.append(f"Start: {start_line}")
    if end_line:
        summary_lines.append(f"End: {end_line}")
    summary_lines.append("")
    summary_lines.append("Generated Files:")
    summary_lines.extend(files)
    summary_lines.append("")
    summary_lines.append("Metrics:")
    summary_lines.append(metrics_text or "<metrics not found>")

    SUMMARY_PATH.write_text("\n".join(summary_lines), encoding="utf-8")
    print(f"Wrote summary to {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
