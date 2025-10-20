## Processed Data Analysis

### Files
- `data/processed/usedcars_clean.csv`
- `data/processed/usedcars_profile.json`

### Summary
- **Rows**: 5,482
- **Columns**: 15
- **Key Categorical Cardinalities**:
  - `Make`: 57
  - `Type`: 349
  - `Region`: 27
  - `Fuel_Type`: 3; `Gear_Type`: 2; `Options`: 3; `Color`: 15
- **Numeric Highlights**:
  - `Year`: 32 unique (cleaned to 1990–2025)
  - `Mileage`: 1,714 unique
  - `Price`: 540 unique (zeros treated as missing and removed)
  - Derived: `Vehicle_Age`, `Price_per_km`

### Data Quality Notes
- No missing values remain in required fields (`Price`, `Year`) after cleaning.
- Duplicates removed.
- String fields standardized to title case.

### Next Steps
- Encode categories (e.g., target-mean or one-hot) for modeling.
- Winsorize or log-transform `Price_per_km` if skewed.
- Validate business ranges (engine sizes, extreme prices/mileages).
