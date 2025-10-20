## Preprocessing Plan (Used Cars SA)

### Goals
- Clean the data so it is ready for analysis and modeling.
- Fix types, handle missing values, and standardize key fields.

### Input
- `data/raw/UsedCarsSA_Clean_EN.csv`

### Output
- `data/processed/usedcars_clean.csv`
- `data/processed/usedcars_profile.json` (basic counts and quality stats)

### Steps
1. Read CSV with a safe parser and header.
2. Set data types:
   - `Year`, `Mileage`, `Price` as numbers
   - `Engine_Size` as float
   - `Negotiable` as boolean
   - others as strings (categories)
3. Trim strings and standardize case (e.g., title case for `Make`, `Type`, `Color`, `Region`).
4. Handle missing or odd values:
   - Treat `Price = 0` as missing (NA)
   - Drop rows with missing `Price` or `Year`
   - Keep `Mileage >= 0` and reasonable `Year` (1990–2025)
5. Remove exact duplicate rows.
6. Add helper features:
   - `Vehicle_Age = 2025 - Year`
   - `Price_per_km = Price / max(Mileage, 1)`
7. Save cleaned data and a simple profile with row count, column types, missing rates, and unique counts.

### Notes
- If the file has fewer rows than expected (~35k in docs), confirm the data source. This plan still works for subsets. 
