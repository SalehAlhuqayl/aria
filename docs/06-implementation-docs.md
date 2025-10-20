## Implementation Documentation

### Modules
- `src/utils.py`: Logging, paths, JSON/joblib I/O, seed control, train/val/test split
- `src/feature_engineering.py`: Build preprocessing (`ColumnTransformer`), feature/target split
- `src/models.py`: Pipelines for Ridge/Lasso, RandomForest, XGBoost with preprocessing
- `src/evaluation.py`: RMSE, MAE, R^2 evaluation helpers
- `src/visualization.py`: Save histograms, scatter, residual plots
- `src/pipeline.py`: End-to-end training/evaluation across models; save metrics and models

### Key Methods
- Preprocessing: one-hot encode categoricals (limited categories for high-cardinality), scale numeric
- Models: linear (Ridge/Lasso), tree ensemble (RF), gradient boosted trees (XGB)
- Split: quantile-binned stratification on target to stabilize regression splits

### Configuration
- Target: `Price`
- Features:
  - Categorical low: `Fuel_Type`, `Gear_Type`, `Options`
  - Categorical high: `Make`, `Type`, `Region`
  - Numeric: `Year`, `Mileage`, `Engine_Size`, `Vehicle_Age`, `Price_per_km`
- Random seed: 42; CV: internal holdout with train/val/test

### Outputs
- Models: `output/models/{ridge,lasso,rf,xgb}.joblib`
- Metrics: `output/results/metrics.json` (val/test RMSE, MAE, R^2)
- Logs: `output/logs/run_experiment.log`
- Figures: `output/figures/*.png`

### Code Structure
- All training uses `sklearn` Pipelines with a shared preprocessing block
- Metrics and models are saved to allow later inference and comparison
- Figures give quick checks on data and model behavior

### Notes
- If performance drifts, tune hyperparameters (trees: depth, n_estimators; linear: regularization)
- For explainability, add SHAP for the best model and partial dependence plots
