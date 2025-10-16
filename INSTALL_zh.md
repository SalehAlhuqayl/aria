# 安装指南

本指南提供使用 ARIA 所需的基础工具的详细安装步骤。

## 概述

你需要安装以下工具：

1. **Git** - 版本控制系统
2. **Python 3.12+** - 编程语言运行环境
3. **UV** - 快速的 Python 包管理器

---

## 1. 安装 Git

Git 用于克隆代码仓库和版本控制。

### Windows

1. 从 [git-scm.com](https://git-scm.com/download/win) 下载 Git
2. 使用默认设置运行安装程序
3. 安装后重启终端

### macOS

**方案 A：使用 Homebrew（推荐）**

```bash
brew install git
```

**方案 B：使用 Xcode 命令行工具**

```bash
xcode-select --install
```

**方案 C：下载安装包**

从 [git-scm.com](https://git-scm.com/download/mac) 下载

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install git
```

### 验证安装

```bash
git --version
# 预期输出：git version 2.x.x 或更高版本
```

---

## 2. 安装 Python 3.12

选择以下安装方法之一：

### 方案 A：直接安装

**Windows：**

1. 访问 [python.org/downloads](https://www.python.org/downloads/)
2. 下载 Python 3.12 或更高版本
3. ⚠️ **重要**：安装时勾选"Add Python to PATH"
4. 完成安装

**macOS：**

```bash
# 使用 Homebrew（推荐）
brew install python@3.12

# 验证安装
python3 --version
```

**Linux (Ubuntu/Debian)：**

```bash
sudo apt-get update
sudo apt-get install python3.12 python3.12-venv python3.12-dev
```

### 方案 B：使用 pyenv（推荐用于管理多版本）

pyenv 可以让你轻松安装和切换多个 Python 版本。

**macOS/Linux：**

```bash
# 安装 pyenv
curl https://pyenv.run | bash

# 添加到 shell 配置文件
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# 重新加载 shell
source ~/.zshrc

# 安装 Python 3.12
pyenv install 3.12.7

# 设置为全局默认版本
pyenv global 3.12.7
```

**Windows：**

```powershell
# 使用 PowerShell 安装 pyenv-win
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

# 安装 Python 3.12
pyenv install 3.12.7
pyenv global 3.12.7
```

### 验证 Python 安装

```bash
python --version
# 或
python3 --version
# 预期输出：Python 3.12.x 或更高版本
```

---

## 3. 安装 UV 包管理器

UV 是一个快速的 Python 包安装器和解析器，设计为 pip 的替代品。

### 所有平台

**Linux/macOS：**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)：**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 验证 UV 安装

```bash
uv --version
# 预期输出：uv x.x.x
```

如果提示命令未找到，请重启终端后再试。

---

## 4. 验证完整安装

运行以下命令确保所有工具已正确安装：

```bash
# 检查 Git
git --version

# 检查 Python
python --version
# 或
python3 --version

# 检查 UV
uv --version

# 检查 pyenv（如果已安装）
pyenv --version
```

所有命令都应返回版本信息，不应有错误。

---

## 安装后快速开始

所有工具安装完成后：

1. **克隆 ARIA 仓库：**

   ```bash
   # 从 GitHub 克隆
   git clone https://github.com/Biaoo/aria.git
   cd aria

   # 或从 Gitee 克隆（国内用户）
   git clone https://gitee.com/BiaooGitee/aria.git
   cd aria
   ```

2. **设置项目依赖：**

   ```bash
   # 使用 UV 同步依赖
   uv sync
   ```

3. **开始使用 ARIA：**

   参照[快速上手指南](./GETTING_STARTED.md)开始你的研究工作流。

---

## 故障排查

### Git 问题

**找不到命令：**

- Windows：重启终端，检查 Git 是否在 PATH 中
- macOS/Linux：尝试通过包管理器安装

### Python 问题

**找不到 Python 命令：**

- Windows：重新安装 Python 并勾选"Add to PATH"
- macOS/Linux：使用 `python3` 而不是 `python`
- 如果使用 pyenv：运行 `pyenv global 3.12.7`

**Python 版本不正确：**

```bash
# 检查当前激活的 Python
which python
python --version

# 使用 pyenv
pyenv versions
pyenv global 3.12.7
```

### UV 问题

**找不到命令：**

- 重启终端
- 检查 PATH：`echo $PATH`（macOS/Linux）或 `echo %PATH%`（Windows）
- 重新安装：[UV 安装指南](https://docs.astral.sh/uv/getting-started/installation/)

### pyenv 构建问题

安装必要的依赖：

**macOS：**

```bash
brew install openssl readline sqlite3 xz zlib
```

**Ubuntu/Debian：**

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev
```

---

## 额外资源

- [Git 文档](https://git-scm.com/doc)
- [Python 文档](https://docs.python.org/3/)
- [UV 文档](https://docs.astral.sh/uv/)
- [pyenv GitHub](https://github.com/pyenv/pyenv)
- [ARIA 快速上手指南](./GETTING_STARTED.md)

---

**下一步：** 完成安装后，请继续阅读[快速上手指南](./GETTING_STARTED.md)学习如何使用 ARIA。
