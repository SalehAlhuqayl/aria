import argparse
import logging
from pathlib import Path
import sys

# Ensure project root is on sys.path so `src` can be imported when running from scripts/
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from src.pipeline import train_and_evaluate_all
from src.utils import FIGURES_DIR, ensure_output_dirs, load_processed_csv, setup_logging
from src.visualization import save_histogram, save_scatter


def main(seed: int = 42) -> None:
    log_path = setup_logging("run_experiment")
    logging.info("Starting experiment run")

    results = train_and_evaluate_all(seed=seed)
    logging.info("Finished training models")
    logging.info(f"Validation/Test metrics saved; results: {results}")

    # Create a few quick figures from processed data
    df = load_processed_csv()
    ensure_output_dirs()
    save_histogram(df, "Price", title="Distribution of Price")
    save_histogram(df, "Mileage", title="Distribution of Mileage")
    if "Year" in df.columns:
        save_histogram(df, "Year", title="Distribution of Year")
    if set(["Mileage", "Price"]).issubset(df.columns):
        save_scatter(df, x="Mileage", y="Price", title="Price vs Mileage")

    logging.info(f"Figures saved in {FIGURES_DIR}")
    logging.info("Run complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run training and evaluation experiment")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    main(seed=args.seed)
