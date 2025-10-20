"""Feature engineering components and preprocessing pipeline."""
from __future__ import annotations

from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_preprocessor(
    categorical_low_card: List[str],
    categorical_high_card: List[str],
    numeric_features: List[str],
) -> ColumnTransformer:
    """Build a ColumnTransformer that encodes categorical and scales numeric features.

    High-cardinality categories are frequency-encoded using a simple custom transformer
    implemented via a Pipeline + OneHot with min frequency threshold when available.
    """
    # For simplicity and stability across environments, use OneHot for all categoricals.
    # If cardinality is too high, we can limit categories by frequency or hash encode.

    ohe_low = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    ohe_high = OneHotEncoder(handle_unknown="ignore", sparse_output=False, max_categories=100)

    numeric_pipe = Pipeline(steps=[
        ("scaler", StandardScaler()),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat_low", ohe_low, categorical_low_card),
            ("cat_high", ohe_high, categorical_high_card),
            ("num", numeric_pipe, numeric_features),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )
    return preprocessor


def split_feature_target(df: pd.DataFrame, target_col: str) -> Tuple[pd.DataFrame, pd.Series]:
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y
