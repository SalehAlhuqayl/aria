## Analysis: output/results/metrics.json

### Key Numbers (Test Set)
- Ridge: RMSE 40,756 | MAE 23,598 | R^2 0.689
- Lasso: RMSE 40,833 | MAE 23,596 | R^2 0.688
- Random Forest: RMSE 17,172 | MAE 6,457 | R^2 0.945
- XGBoost: RMSE 13,728 | MAE 5,432 | R^2 0.965

### Findings
- Tree-based models greatly outperform linear models, suggesting non-linear effects and interactions.
- XGBoost is the best overall with the lowest errors and highest R^2.
- The gap between RF and XGB points to benefits from boosted trees and tuned learning rate/depth.

### Implications
- Use XGBoost as the primary model for deployment and analysis.
- Next, perform feature importance and SHAP analysis to explain predictions.
- Consider modest hyperparameter tuning for further gains or faster inference.
