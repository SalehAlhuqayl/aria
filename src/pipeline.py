"""Experiment pipeline for training and evaluation."""
from __future__ import annotations

from dataclasses import asdict
from typing import Dict, List

import numpy as np
import pandas as pd
from sklearn.base import RegressorMixin

from .evaluation import RegressionReport, evaluate_model
from .feature_engineering import split_feature_target
from .models import (
    build_linear_model_pipeline,
    build_random_forest_pipeline,
    build_xgb_pipeline,
)
from .utils import (
    MODELS_DIR,
    RESULTS_DIR,
    ensure_output_dirs,
    load_processed_csv,
    save_joblib,
    save_json,
    set_global_seed,
    train_val_test_split,
)


TARGET = "Price"
CATEGORICAL_LOW = ["Fuel_Type", "Gear_Type", "Options"]
CATEGORICAL_HIGH = ["Make", "Type", "Region"]
NUMERIC = ["Year", "Mileage", "Engine_Size", "Vehicle_Age", "Price_per_km"]


def train_and_evaluate_all(seed: int = 42) -> Dict[str, Dict]:
    ensure_output_dirs()
    set_global_seed(seed)

    df = load_processed_csv()
    X, y = split_feature_target(df, TARGET)

    # Align with feature lists (drop any columns not referenced)
    cols_needed = list(set(CATEGORICAL_LOW + CATEGORICAL_HIGH + NUMERIC))
    X = X[[c for c in cols_needed if c in X.columns]].copy()

    # Split
    split = train_val_test_split(pd.concat([X, y], axis=1), target_col=TARGET, seed=seed)

    # Build models
    models: Dict[str, RegressorMixin] = {
        "ridge": build_linear_model_pipeline(CATEGORICAL_LOW, CATEGORICAL_HIGH, NUMERIC, kind="ridge"),
        "lasso": build_linear_model_pipeline(CATEGORICAL_LOW, CATEGORICAL_HIGH, NUMERIC, kind="lasso"),
        "rf": build_random_forest_pipeline(CATEGORICAL_LOW, CATEGORICAL_HIGH, NUMERIC),
        "xgb": build_xgb_pipeline(CATEGORICAL_LOW, CATEGORICAL_HIGH, NUMERIC),
    }

    results: Dict[str, Dict] = {}

    for name, model in models.items():
        model.fit(split.X_train, split.y_train)
        val_report = evaluate_model(model, split.X_val, split.y_val)
        test_report = evaluate_model(model, split.X_test, split.y_test)

        # Save model and metrics
        save_joblib(model, MODELS_DIR / f"{name}.joblib")
        results[name] = {
            "val": asdict(val_report),
            "test": asdict(test_report),
        }

    # Save results JSON
    save_json(results, RESULTS_DIR / "metrics.json")
    return results
