# INSTALL.md

本文件提供项目的安装说明。

## 先决条件

- Python 3.12
- uv（https://docs.astral.sh/uv/）
- git

## 安装步骤

### 克隆仓库

```bash
git clone https://github.com/your-username/your-repository.git
```

### 安装 UV 及依赖

```bash
curl -fsSL https://astral.sh/uv/install.sh | sh
```

### 创建虚拟环境

```bash
# 使用 Python 3.12 作为默认解释器
uv venv --python 3.12
```

### 安装默认依赖

```bash
uv add numpy openpyxl pandas scikit-learn joblib matplotlib seaborn xgboost gradio
```

（可选）如需使用清华镜像加速安装：

```bash
UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv add numpy openpyxl pandas scikit-learn joblib matplotlib seaborn xgboost gradio
```

### 同步依赖

```bash
uv sync
```
