## Experiment Report

### Executive Summary
We trained models to predict used car prices in Saudi Arabia. XGBoost performed best with low error and high R^2. Results suggest strong non-linear effects.

### Methodology
- Data: `data/processed/usedcars_clean.csv` (5,482 rows, 15 columns)
- Target: `Price`
- Features: brand, model type, year, mileage, region, fuel, gear, engine size, options, and engineered features
- Split: Train/validation/test with a fixed random seed (42)
- Models: Ridge, Lasso, Random Forest, XGBoost; preprocessing via `sklearn` pipelines

### Results (Test)
- Ridge: RMSE 40,756 | MAE 23,598 | R^2 0.689
- Lasso: RMSE 40,833 | MAE 23,596 | R^2 0.688
- Random Forest: RMSE 17,172 | MAE 6,457 | R^2 0.945
- XGBoost: RMSE 13,728 | MAE 5,432 | R^2 0.965

### Key Findings
- XGBoost is the top model and should be the default choice.
- Non-linear models fit the data better than linear models.
- Mileage and year (vehicle age) show strong relationships with price.

### Limitations
- Dataset may be a subset of the expected full data (~35k rows); results may shift with more data.
- We did minimal hyperparameter tuning; there is room to improve.

### Next Steps
- Add SHAP explainability and partial dependence plots for the best model.
- Try simple tuning to balance accuracy and speed.
- Build an inference script to score new listings.
