"""Utility helpers: logging, paths, I/O, and reproducibility.

This module centralizes common helpers used across the pipeline. It avoids
external heavy dependencies to keep the project lightweight.
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import joblib
import numpy as np
import pandas as pd


# Default project paths
DATA_DIR = Path("data")
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = Path("output")
MODELS_DIR = OUTPUT_DIR / "models"
RESULTS_DIR = OUTPUT_DIR / "results"
FIGURES_DIR = OUTPUT_DIR / "figures"
LOGS_DIR = OUTPUT_DIR / "logs"


def ensure_output_dirs() -> None:
    """Create required output directories if they do not exist."""
    for d in [OUTPUT_DIR, MODELS_DIR, RESULTS_DIR, FIGURES_DIR, LOGS_DIR]:
        d.mkdir(parents=True, exist_ok=True)


def setup_logging(log_name: str = "experiment") -> Path:
    """Set up simple file and console logging.

    Returns the path of the log file.
    """
    ensure_output_dirs()
    log_file = LOGS_DIR / f"{log_name}.log"

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Clear existing handlers to avoid duplicates during repeated runs
    logger.handlers = []

    fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

    logging.info("Logging initialized")
    return log_file


@dataclass
class DatasetSplit:
    """Container for dataset splits."""
    X_train: pd.DataFrame
    X_val: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_val: pd.Series
    y_test: pd.Series


def load_processed_csv(path: Path | str = PROCESSED_DIR / "usedcars_clean.csv") -> pd.DataFrame:
    """Load processed dataset as DataFrame."""
    return pd.read_csv(path)


def save_json(data: Dict[str, Any], path: Path | str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def save_joblib(obj: Any, path: Path | str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(obj, path)


def set_global_seed(seed: int = 42) -> None:
    np.random.seed(seed)


def train_val_test_split(
    df: pd.DataFrame,
    target_col: str,
    seed: int = 42,
    train_size: float = 0.7,
    val_size: float = 0.15,
) -> DatasetSplit:
    """Split into train/val/test preserving class-like structure via quantile bins on target.

    For regression, approximate stratification by binning the target into quantiles.
    """
    from sklearn.model_selection import train_test_split

    set_global_seed(seed)

    # Create bins for stratification
    y = df[target_col].values
    # Use 10 quantile bins; handle duplicates gracefully
    try:
        bins = pd.qcut(df[target_col], q=min(10, df.shape[0]), duplicates="drop")
    except Exception:
        bins = None

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        df.drop(columns=[target_col]),
        df[target_col],
        test_size=1.0 - (train_size + val_size),
        random_state=seed,
        stratify=bins if bins is not None else None,
    )

    # Recompute bins on the train_val subset for val split
    try:
        bins_tv = pd.qcut(y_train_val, q=min(10, len(y_train_val)), duplicates="drop")
    except Exception:
        bins_tv = None

    rel_val_size = val_size / (train_size + val_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val,
        y_train_val,
        test_size=rel_val_size,
        random_state=seed,
        stratify=bins_tv if bins_tv is not None else None,
    )

    return DatasetSplit(
        X_train=X_train,
        X_val=X_val,
        X_test=X_test,
        y_train=y_train,
        y_val=y_val,
        y_test=y_test,
    )
