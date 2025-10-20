"""Model builders returning sklearn Pipelines with preprocessing."""
from __future__ import annotations

from typing import List

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso, Ridge
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

from .feature_engineering import build_preprocessor


def build_linear_model_pipeline(
    categorical_low_card: List[str],
    categorical_high_card: List[str],
    numeric_features: List[str],
    kind: str = "ridge",
) -> Pipeline:
    preprocessor = build_preprocessor(categorical_low_card, categorical_high_card, numeric_features)
    if kind == "ridge":
        model = Ridge(alpha=1.0, random_state=42)
    elif kind == "lasso":
        model = Lasso(alpha=0.001, random_state=42, max_iter=10000)
    else:
        raise ValueError("kind must be 'ridge' or 'lasso'")

    pipe = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", model),
    ])
    return pipe


def build_random_forest_pipeline(
    categorical_low_card: List[str],
    categorical_high_card: List[str],
    numeric_features: List[str],
) -> Pipeline:
    preprocessor = build_preprocessor(categorical_low_card, categorical_high_card, numeric_features)
    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=None,
        n_jobs=-1,
        random_state=42,
    )
    pipe = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", model),
    ])
    return pipe


def build_xgb_pipeline(
    categorical_low_card: List[str],
    categorical_high_card: List[str],
    numeric_features: List[str],
) -> Pipeline:
    preprocessor = build_preprocessor(categorical_low_card, categorical_high_card, numeric_features)
    model = XGBRegressor(
        n_estimators=500,
        max_depth=8,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        random_state=42,
        n_jobs=-1,
        tree_method="hist",
    )
    pipe = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", model),
    ])
    return pipe
