"""Visualization helpers for EDA and model diagnostics."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .utils import FIGURES_DIR


def save_histogram(df: pd.DataFrame, column: str, title: Optional[str] = None) -> Path:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(6, 4))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(title or f"Distribution of {column}")
    plt.tight_layout()
    out = FIGURES_DIR / f"hist_{column}.png"
    plt.savefig(out, dpi=150)
    plt.close()
    return out


def save_scatter(df: pd.DataFrame, x: str, y: str, title: Optional[str] = None) -> Path:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x=x, y=y, s=10, alpha=0.6)
    plt.title(title or f"{y} vs {x}")
    plt.tight_layout()
    out = FIGURES_DIR / f"scatter_{x}_vs_{y}.png"
    plt.savefig(out, dpi=150)
    plt.close()
    return out


def save_residual_plot(y_true, y_pred, title: Optional[str] = None) -> Path:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(6, 4))
    residuals = y_true - y_pred
    sns.scatterplot(x=y_pred, y=residuals, s=10, alpha=0.6)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Predicted")
    plt.ylabel("Residuals")
    plt.title(title or "Residual Plot")
    plt.tight_layout()
    out = FIGURES_DIR / "residuals.png"
    plt.savefig(out, dpi=150)
    plt.close()
    return out
