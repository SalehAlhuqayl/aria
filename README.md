# Used Car Price Modeling (Saudi Arabia)

This repository contains the code and manuscript for a study on used car prices in Saudi Arabia.

## Contents
- `docs/10-manuscript.md` – Manuscript (with embedded figures)
- `output/paper/paper.pdf` – PDF export of the manuscript
- `output/paper/index.html` – HTML export of the manuscript
- `src/` – Source code (feature engineering, models, evaluation, pipeline)
- `scripts/` – Utility scripts (preprocess, run experiment, export paper)
- `data/` – Data folders (`raw/`, `processed/`, and generated `output/`)

## Quick Start
1. Install Python 3.12 and required packages:
   ```bash
   pip install -r requirements.txt
   # or
   pip install pandas numpy scikit-learn xgboost matplotlib seaborn joblib markdown
   ```
2. Preprocess data and run the experiment:
   ```bash
   python scripts/preprocess_usedcars.py
   python scripts/run_experiment.py --seed 42
   ```
3. Export paper (HTML already generated; PDF created via Edge headless):
   ```bash
   python scripts/export_paper.py
   ```

## License
See `LICENSE`.
