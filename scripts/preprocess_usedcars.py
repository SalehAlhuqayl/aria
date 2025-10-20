import argparse
import json
import os
from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/UsedCarsSA_Clean_EN.csv")
PROCESSED_DIR = Path("data/processed")
CLEAN_PATH = PROCESSED_DIR / "usedcars_clean.csv"
PROFILE_PATH = PROCESSED_DIR / "usedcars_profile.json"
CURRENT_YEAR = 2025


def standardize_title_case(value: str) -> str:
    if pd.isna(value):
        return value
    # Keep acronyms reasonably formatted by title-casing words
    return str(value).strip().title()


def coerce_bool_from_str(value):
    if pd.isna(value):
        return pd.NA
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "t", "1", "yes", "y"}:
        return True
    if text in {"false", "f", "0", "no", "n"}:
        return False
    return pd.NA


def load_raw_dataframe(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(
        csv_path,
        dtype={
            # read as objects first; we will coerce later to handle odd values
            "Make": "string",
            "Type": "string",
            "Origin": "string",
            "Color": "string",
            "Options": "string",
            "Fuel_Type": "string",
            "Gear_Type": "string",
            "Region": "string",
            "Year": "Int64",
            "Mileage": "Int64",
            "Engine_Size": "float64",
            "Price": "Int64",
            "Negotiable": "string",
        },
        keep_default_na=True,
    )
    return df


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize text columns
    for col in [
        "Make",
        "Type",
        "Origin",
        "Color",
        "Options",
        "Fuel_Type",
        "Gear_Type",
        "Region",
    ]:
        if col in df.columns:
            df[col] = df[col].astype("string").map(standardize_title_case)

    # Coerce booleans
    if "Negotiable" in df.columns:
        df["Negotiable"] = df["Negotiable"].map(coerce_bool_from_str)

    # Numeric coercions and guards
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
        df.loc[(df["Year"] < 1990) | (df["Year"] > CURRENT_YEAR), "Year"] = pd.NA

    if "Mileage" in df.columns:
        df["Mileage"] = pd.to_numeric(df["Mileage"], errors="coerce").astype("Int64")
        df.loc[df["Mileage"] < 0, "Mileage"] = pd.NA

    if "Engine_Size" in df.columns:
        df["Engine_Size"] = pd.to_numeric(df["Engine_Size"], errors="coerce").astype("float64")

    if "Price" in df.columns:
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce").astype("Int64")
        # Treat 0 price as missing
        df.loc[df["Price"] == 0, "Price"] = pd.NA

    # Drop rows missing critical targets
    required_columns = [c for c in ["Price", "Year"] if c in df.columns]
    if required_columns:
        df = df.dropna(subset=required_columns)

    # Remove duplicates
    df = df.drop_duplicates().reset_index(drop=True)

    # Derived features
    if "Year" in df.columns:
        df["Vehicle_Age"] = CURRENT_YEAR - df["Year"].astype("Int64")

    if "Mileage" in df.columns and "Price" in df.columns:
        denominator = df["Mileage"].where(df["Mileage"] > 0, other=1)
        df["Price_per_km"] = (df["Price"].astype("float64") / denominator).round(6)

    return df


def generate_profile(df: pd.DataFrame) -> dict:
    profile: dict[str, dict] = {
        "row_count": int(df.shape[0]),
        "column_count": int(df.shape[1]),
        "columns": {},
    }
    for column in df.columns:
        series = df[column]
        profile["columns"][column] = {
            "dtype": str(series.dtype),
            "num_missing": int(series.isna().sum()),
            "pct_missing": float((series.isna().mean() * 100.0)),
            "num_unique": int(series.nunique(dropna=True)),
            "example_values": [
                *(series.dropna().astype(str).head(3).tolist())
            ],
        }
    return profile


def ensure_processed_dir():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def main(raw_csv: str | None = None, out_csv: str | None = None):
    csv_path = Path(raw_csv) if raw_csv else RAW_PATH
    out_path = Path(out_csv) if out_csv else CLEAN_PATH

    ensure_processed_dir()

    if not csv_path.exists():
        raise FileNotFoundError(f"Raw CSV not found: {csv_path}")

    df_raw = load_raw_dataframe(csv_path)
    df_clean = clean_dataframe(df_raw)

    # Save outputs
    df_clean.to_csv(out_path, index=False)

    profile = generate_profile(df_clean)
    with open(PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

    print(f"Wrote cleaned CSV: {out_path}")
    print(f"Wrote profile JSON: {PROFILE_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess Used Cars SA dataset")
    parser.add_argument("--raw", type=str, default=None, help="Path to raw CSV")
    parser.add_argument("--out", type=str, default=None, help="Path to output cleaned CSV")
    args = parser.parse_args()
    main(raw_csv=args.raw, out_csv=args.out)
