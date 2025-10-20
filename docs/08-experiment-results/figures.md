## Analysis: output/figures/*

### Files
- `hist_Price.png`: Price is right-skewed; consider log transform for linear models.
- `hist_Mileage.png`: Wide range; outliers exist at high mileage.
- `hist_Year.png`: Most cars are recent (2010+); model should use `Vehicle_Age`.
- `scatter_Mileage_vs_Price.png`: Negative trend; price generally drops as mileage rises.

### Next Visuals
- Residual plots for best model
- Feature importance and SHAP summary for XGBoost
- Box plots of price by `Make` and `Region`
