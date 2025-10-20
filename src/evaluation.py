"""Evaluation utilities for regression models."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np
from sklearn.base import RegressorMixin
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


@dataclass
class RegressionReport:
    rmse: float
    mae: float
    r2: float


def evaluate_predictions(y_true: np.ndarray, y_pred: np.ndarray) -> RegressionReport:
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    r2 = float(r2_score(y_true, y_pred))
    return RegressionReport(rmse=rmse, mae=mae, r2=r2)


def evaluate_model(model: RegressorMixin, X, y) -> RegressionReport:
    y_pred = model.predict(X)
    return evaluate_predictions(np.asarray(y), np.asarray(y_pred))
