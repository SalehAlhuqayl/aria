## Raw Data Analysis

### Dataset Inventory
- **Files**: 1 (`data/raw/UsedCarsSA_Clean_EN.csv`)
- **Format**: CSV (comma-separated, header present)
- **Size (bytes)**: 662,888
- **Total lines**: 9 (including header)
- **Estimated rows**: 8 data rows

### Columns (from header)
Make, Type, Year, Origin, Color, Options, Engine_Size, Fuel_Type, Gear_Type, Mileage, Region, Price, Negotiable

### Inferred Data Types
- **Make / Type / Origin / Color / Options / Fuel_Type / Gear_Type / Region**: categorical strings
- **Year**: integer year
- **Engine_Size**: decimal liters (float)
- **Mileage**: integer kilometers
- **Price**: integer SAR (some zeros present)
- **Negotiable**: boolean

### Notable Characteristics
- Some records have `Price = 0` (likely missing/placeholder; treat as NA or filter).
- Fuel types include `Gas`, `Diesel`, and `Hybrid`.
- Regions include major cities (e.g., Riyadh, Jeddah, Dammam).
- Mixed option levels: `Standard`, `Semi Full`, `Full`.

### Basic Quality Checks
- Header detected and consistent with sample rows.
- No obvious delimiter issues in first 50 lines.
- Data volume appears small in this snapshot; cross-check against project doc estimate (≈35k rows) to confirm if this is a subset.

### Next Steps
- Load CSV with a robust parser and enforce dtypes.
- Normalize categorical values (e.g., color naming, options levels).
- Treat `Price = 0` as missing if appropriate.
- Profile distributions for `Year`, `Mileage`, and `Price`.
- Validate row count vs. expected (~35k) and reconcile data source if mismatch persists.
