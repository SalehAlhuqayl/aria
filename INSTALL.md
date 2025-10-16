# INSTALL.md

This file provides instructions for installing the project.

## Prerequisites

- Python 3.10
- uv(`https://docs.astral.sh/uv/`)
- git

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### Install UV and the dependencies

```bash
curl -fsSL https://astral.sh/uv/install.sh | sh
```

### Set up the virtual environment

```bash
# Use python 3.10 default interpreter
uv venv --python 3.10
```

### Install the default dependencies

```bash
uv add numpy openpyxl pandas scikit-learn joblib matplotlib seaborn xgboost gradio
```

Optional: use the Tsinghua PyPI mirror for faster installation:

```bash
UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv add numpy openpyxl pandas scikit-learn joblib matplotlib seaborn xgboost gradio
```

### Sync the dependencies

```bash
uv sync
```
