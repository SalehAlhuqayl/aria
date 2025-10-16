# Installation Guide

This guide provides step-by-step instructions for installing the essential tools needed to use ARIA.

## Overview

You'll need to install the following tools:

1. **Git** - Version control system
2. **Python 3.12+** - Programming language runtime
3. **UV** - Fast Python package manager

---

## 1. Install Git

Git is required for cloning the repository and version control.

### Windows

1. Download Git from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer with default settings
3. Restart your terminal after installation

### macOS

**Option A: Using Homebrew (Recommended)**

```bash
brew install git
```

**Option B: Using Xcode Command Line Tools**

```bash
xcode-select --install
```

**Option C: Download Installer**

Download from [git-scm.com](https://git-scm.com/download/mac)

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install git
```

### Verify Installation

```bash
git --version
# Expected output: git version 2.x.x or higher
```

---

## 2. Install Python 3.12

Choose one of the following installation methods:

### Option A: Direct Installation

**Windows:**

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.12 or higher
3. ⚠️ **Important**: Check "Add Python to PATH" during installation
4. Complete the installation

**macOS:**

```bash
# Using Homebrew (recommended)
brew install python@3.12

# Verify installation
python3 --version
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt-get update
sudo apt-get install python3.12 python3.12-venv python3.12-dev
```

### Option B: Using pyenv (Recommended for Multiple Versions)

pyenv allows you to easily install and switch between multiple Python versions.

**macOS/Linux:**

```bash
# Install pyenv
curl https://pyenv.run | bash

# Add to shell configuration
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Reload shell
source ~/.zshrc

# Install Python 3.12
pyenv install 3.12.7

# Set as global default
pyenv global 3.12.7
```

**Windows:**

```powershell
# Install pyenv-win using PowerShell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

# Install Python 3.12
pyenv install 3.12.7
pyenv global 3.12.7
```

### Verify Python Installation

```bash
python --version
# or
python3 --version
# Expected output: Python 3.12.x or higher
```

---

## 3. Install UV Package Manager

UV is a fast Python package installer and resolver, designed as a drop-in replacement for pip.

### All Platforms

**Linux/macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify UV Installation

```bash
uv --version
# Expected output: uv x.x.x
```

If command not found, restart your terminal and try again.

---

## 4. Verify Complete Installation

Run the following commands to ensure everything is installed:

```bash
# Check Git
git --version

# Check Python
python --version
# or
python3 --version

# Check UV
uv --version

# Check pyenv (if installed)
pyenv --version
```

All commands should return version information without errors.

---

## Quick Start After Installation

Once all tools are installed:

1. **Clone ARIA repository:**

   ```bash
   # From GitHub
   git clone https://github.com/Biaoo/aria.git
   cd aria

   # OR from Gitee (China users)
   git clone https://gitee.com/BiaooGitee/aria.git
   cd aria
   ```

2. **Set up project dependencies:**

   ```bash
   # Sync dependencies using UV
   uv sync
   ```

3. **Start using ARIA:**

   Follow the [Getting Started Guide](./GETTING_STARTED.md) to begin your research workflow.

---

## Troubleshooting

### Git Issues

**Command not found:**

- Windows: Restart terminal, check if Git is in PATH
- macOS/Linux: Try installing via package manager

### Python Issues

**Python command not found:**

- Windows: Reinstall Python with "Add to PATH" checked
- macOS/Linux: Use `python3` instead of `python`
- If using pyenv: Run `pyenv global 3.12.7`

**Wrong Python version:**

```bash
# Check which Python is active
which python
python --version

# With pyenv
pyenv versions
pyenv global 3.12.7
```

### UV Issues

**Command not found:**

- Restart your terminal
- Check PATH: `echo $PATH` (macOS/Linux) or `echo %PATH%` (Windows)
- Reinstall: [UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)

### pyenv Build Issues

Install required dependencies:

**macOS:**

```bash
brew install openssl readline sqlite3 xz zlib
```

**Ubuntu/Debian:**

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev
```

---

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [Python Documentation](https://docs.python.org/3/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [pyenv GitHub](https://github.com/pyenv/pyenv)
- [ARIA Getting Started Guide](./GETTING_STARTED.md)

---

**Next Step:** After completing this installation, proceed to [GETTING_STARTED.md](./GETTING_STARTED.md) to learn how to use ARIA.
