## Research Plan

### Goal
Predict used car prices in Saudi Arabia and explain price differences across brands, years, regions, and mileage.

### Feature Engineering Plan
- **Core features**: `Make`, `Type`, `Year`, `Mileage`, `Region`, `Fuel_Type`, `Gear_Type`, `Engine_Size`, `Options`
- **Derived features**: `Vehicle_Age = 2025 - Year`, `Price_per_km`, log of `Price`
- **Encodings**:
  - One-hot for low-cardinality: `Fuel_Type`, `Gear_Type`, `Options`
  - Target or frequency encoding for high-cardinality: `Type`, `Make`
  - Region grouping if needed (e.g., top 10 regions vs. other)
- **Numeric scaling**: Standardize `Mileage`, `Engine_Size`, `Vehicle_Age` for linear models
- **Outlier handling**: Winsorize extreme `Price`, `Mileage`; optional log-transform `Price`

### Analysis/Model Architecture
- **Baseline**: Linear Regression (with regularization: Ridge/Lasso)
- **Tree models**: Random Forest Regressor, XGBoost Regressor
- **Explainability**: SHAP values and permutation importance; Partial Dependence and ICE plots
- **Model selection**: Compare via cross-validation; keep best by validation metric

### Evaluation Framework
- **Primary metrics**: RMSE, MAE
- **Secondary metrics**: R^2, MAPE (report with caution on small prices)
- **Validation**: Stratified K-fold by `Make` or `Year` buckets to balance data; 5-fold CV
- **Fairness/robustness checks**: Error by `Make`, `Region`, and `Year` bands

### Experiment Pipeline
1. Load processed data from `data/processed/usedcars_clean.csv`
2. Split train/validation/test (e.g., 70/15/15) with stratification
3. Build preprocessing transformers (encoders, scalers) with `sklearn` pipelines
4. Train models: Linear (Ridge/Lasso), RandomForest, XGBoost (basic hyperparams)
5. Tune selected model(s) with grid or Bayesian search (small search first)
6. Evaluate on validation and holdout test set; log metrics and artifacts
7. Explain results: feature importances, SHAP, and partial dependence
8. Save best model and pipeline to `output/models/`

### Visualization Requirements
- Distributions: `Price`, `Mileage`, `Year`, `Vehicle_Age`
- Relationships: `Price` vs. `Mileage`, `Price` vs. `Year` (with regression lines)
- Categorical effects: Box/violin plots by `Make`, `Region`, `Fuel_Type`
- Model diagnostics: Residual plots, predicted vs. actual
- Explainability: SHAP summary, dependence plots

### Task Breakdown (for implementation)
- Build data module to load/split data with reproducible seed
- Implement encoders and scalers inside `sklearn` pipelines
- Implement baseline models and evaluation loop
- Add hyperparameter search for top models
- Create plots and save to `output/figures/`
- Save best model and metrics to `output/models/` and `output/results/`

### Resources and Dependencies
- Python 3.12, `pandas`, `numpy`, `scikit-learn`, `xgboost`, `matplotlib`, `seaborn`, `joblib`
- Optional: `shap` for explainability (can be added to dependencies)
- Compute: CPU is enough for this dataset size

### Notes
- If the full ~35k dataset becomes available, rerun preprocessing; the plan scales.
- Keep a simple, clear code structure so it is easy to maintain and extend.
