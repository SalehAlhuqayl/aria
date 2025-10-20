## Execution Instructions

### 1) Setup
- Python 3.12 installed
- Install needed packages:
  - `pip install -r requirements.txt` (if available), or
  - `pip install pandas numpy scikit-learn xgboost matplotlib seaborn joblib`

### 2) Data
- Place raw CSV in `data/raw/` named `UsedCarsSA_Clean_EN.csv`
- Run preprocessing:
  - `python scripts/preprocess_usedcars.py`
  - Outputs go to `data/processed/`

### 3) Train and Evaluate
- Run the experiment:
  - `python scripts/run_experiment.py --seed 42`
- Results:
  - Models in `output/models/`
  - Metrics JSON in `output/results/metrics.json`
  - Figures in `output/figures/`
  - Logs in `output/logs/`

### 4) Tips
- If you see import errors, run from the project root folder
- Change `--seed` to test repeatability
- To improve results, try tuning model hyperparameters
