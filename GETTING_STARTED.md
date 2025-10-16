# Getting Started with ARIA

This guide will walk you through the complete process of using ARIA (Automated Research Intelligence Assistant) from setup to generating your first research report.

## Prerequisites

Before starting, you'll need to install the following tools:

- **Python 3.12 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - Version control system [Download Git](https://git-scm.com/downloads)
- **AI Code Editor** - Choose one:
  - [Cursor](https://www.cursor.com/) (Recommended, AI built-in)
  - [Claude Code](https://claude.com/product/claude-code) (AI-powered development tool)
  - [Visual Studio Code](https://code.visualstudio.com/) + AI Extensions
  - [Lingma IDE](https://lingma.aliyun.com/download) (For China users, when Claude Code/Cursor models are not accessible)
- **UV Package Manager** - Fast Python package installer [UV Documentation](https://docs.astral.sh/uv/)
  - Recommended over pip for better performance
  - Installation instructions provided below

### Tool Installation Guide

#### 1. Install Git

**Windows:**

- Download from [git-scm.com](https://git-scm.com/download/win)
- Run the installer with default settings

**macOS:**

```bash
# Using Homebrew (recommended)
brew install git

# Or download from https://git-scm.com/download/mac
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt-get update
sudo apt-get install git
```

Verify installation:

```bash
git --version
```

#### 2. Install Python

**Windows:**

- Download from [python.org](https://www.python.org/downloads/)
- ⚠️ Important: Check "Add Python to PATH" during installation

**macOS:**

```bash
# Using Homebrew (recommended)
brew install python@3.12

# Or download from https://www.python.org/downloads/
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt-get update
sudo apt-get install python3.12 python3.12-venv
```

Verify installation:

```bash
python3 --version  # Should show 3.12 or higher
```

#### 3. Install UV Package Manager

**All Platforms:**

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

For more details, see [UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)

#### 4. Install Code Editor with AI

Choose **ONE** of the following options:

---

**Option A: Cursor**

Cursor is an AI-powered code editor with built-in AI features.

**Features:**

- AI features built-in (no extension installation required)
- Slash command system for easy workflow execution
- Works with Claude, GPT-4, and other AI models
- Based on VSCode

**Installation:**

1. Visit [cursor.com](https://www.cursor.com/)
2. Download the appropriate version for your OS
3. Install the application
4. Open Cursor and sign in (or skip to use without account)
5. Configure your AI model preference in Settings
6. In the chat, type `/` to see available commands and select ARIA workflow commands

---

**Option B: Visual Studio Code + AI Extensions**

If you're already using VSCode or prefer it, you can add AI capabilities through extensions.

**Step 1: Install Visual Studio Code**

- Visit [code.visualstudio.com](https://code.visualstudio.com/)
- Download and install for your operating system

**Step 2: Install AI Extensions** (choose ONE):

**GitHub Copilot** (Supports slash commands)

- Open VSCode
- Go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`)
- Search for "GitHub Copilot" and "GitHub Copilot Chat"
- Click Install on both extensions
- Sign in with your GitHub account
- Type `/` in Copilot Chat to use ARIA workflow commands
- Learn more: [GitHub Copilot](https://github.com/features/copilot)

**OpenAI Codex** (Supports slash commands)

- Open VSCode
- Go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`)
- Search for "OpenAI" or "ChatGPT" extensions
- Click Install and configure with your OpenAI API key
- Type `/` in the chat to use ARIA workflow commands
- Learn more: [OpenAI Platform](https://platform.openai.com/)

**Step 3: Install Python Extension** (Recommended)

- Search for "Python" by Microsoft in Extensions
- Click Install for better Python development support

---

**Option C: Lingma IDE** (For China Users)

Lingma IDE is an AI-powered development tool by Alibaba Cloud's Tongyi team, specifically designed for Chinese users when international AI models (Claude Code/Cursor) are not accessible.

**Features:**

- Full integration with AI coding assistant (built-in, no plugin needed)
- Project-level awareness and code generation
- Inline chat and code suggestions
- Terminal command execution
- Memory and context awareness
- Programming agent capabilities
- Works well in China without VPN

**Installation:**

1. Visit [Lingma IDE Download Page](https://lingma.aliyun.com/download)
2. Download the appropriate version:
   - **macOS**: macOS 10.15+ (Both Intel and Apple Silicon)
   - **Windows**: Windows 10/11 (x86, arm64)
3. Install the application
4. Open Lingma IDE and login with your Aliyun (Alibaba Cloud) account
5. Start using AI coding features immediately

**Using ARIA Commands in Lingma IDE:**

Lingma IDE supports similar workflow commands like Cursor:

1. Open the ARIA project folder in Lingma IDE
2. Use the chat feature to reference ARIA command files
3. Type `@` followed by the command file name (e.g., `@raw-data-analysis.md`)
4. Follow the AI-guided workflow

Learn more: [Lingma IDE Official Site](https://lingma.aliyun.com/download)

---

**Comparison:**

| Feature        | Cursor              | VSCode + Extensions                | Lingma IDE          |
| -------------- | ------------------- | ---------------------------------- | ------------------- |
| AI Built-in    | Yes                 | No (requires extension)            | Yes                 |
| Slash Commands | Native support      | Yes (GitHub Copilot, OpenAI Codex) | @ commands          |
| Setup Steps    | Install editor only | Install editor + extension         | Install editor only |
| China Access   | May require VPN     | Depends on extension               | Optimized for China |
| Customization  | Standard options    | Extensive plugin ecosystem         | Standard options    |

## Step 1: Fork and Clone the Repository

### Option A: Fork on GitHub (Recommended)

1. Visit [ARIA on GitHub](https://github.com/Biaoo/aria)
2. Click the "Fork" button in the top-right corner
3. Clone your forked repository:

```bash
git clone https://github.com/YOUR_USERNAME/aria.git
cd aria
```

### Option B: Fork on Gitee (For China Users)

1. Visit [ARIA on Gitee](https://gitee.com/BiaooGitee/aria)
2. Click the "Fork" button in the top-right corner
3. Clone your forked repository:

```bash
git clone https://gitee.com/YOUR_USERNAME/aria.git
cd aria
```

### Option C: Direct Clone

If you prefer not to fork, you can directly clone from GitHub or Gitee:

**From GitHub:**

```bash
git clone https://github.com/Biaoo/aria.git
cd aria
```

**From Gitee:**

```bash
git clone https://gitee.com/BiaooGitee/aria.git
cd aria
```

## Step 2: Set Up Python Environment

Now that you have all the tools installed, let's set up the Python environment for ARIA:

### Create Virtual Environment

```bash
# Navigate to your ARIA project directory
cd aria

# Create a virtual environment with Python 3.12
uv venv --python 3.12
```

### Activate Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
uv sync
```

**For users in China** (optional, for faster downloads):

```bash
UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv sync
```

### Verify Installation

```bash
# Check if packages are installed correctly
python -c "import pandas; import numpy; import sklearn; print('✓ All packages installed successfully!')"
```

> **Note:** For more advanced configuration options, see [INSTALL.md](./INSTALL.md).

## Step 3: Project Structure Setup

Create the necessary directories if they don't exist:

```bash
mkdir -p data/raw data/processed
mkdir -p docs
mkdir -p data/output/{models,results,figures,logs}
```

## Step 4: Prepare Your Data

1. Place your raw data files in the `data/raw/` directory:

   ```bash
   cp /path/to/your/data/* data/raw/
   ```

2. Create the initial project documentation:

   ```bash
   touch docs/01-basic-information.md
   ```

3. Edit `docs/01-basic-information.md` to include:
   - Project title and objectives
   - Data description and sources
   - Research questions
   - Expected outcomes

Example structure:

```markdown
# Project: [Your Project Name]

## Research Background

### Domain Introduction (optional)

[Describe the field/domain of your research, why this problem is important]

### Research Motivation (optional)

[Why this research is needed, what gaps it addresses]

## Research Objectives (optional)

### Primary Goal (optional)

[Main objective of your research]

### Specific Aims (optional)

1. [First specific aim]
2. [Second specific aim]
3. [Third specific aim]

## Raw Data Description

### Data Source

- Origin: [Where the data comes from - database, experiment, survey, etc.]
- Collection Method: [How the data was collected]
- Time Period: [When the data was collected]
- Geographic Scope: [If applicable]

### Data Characteristics

- File Format: [CSV, JSON, Excel, images, etc.]
- Number of Files: [How many data files]
- Total Size: [File sizes]
- Sample Count: [Number of records/samples]
- Feature Count: [Number of variables/columns]

### Data Structure

- Primary Keys: [Unique identifiers]
- Feature Types: [Numerical, categorical, text, etc.]
- Target Variable: [If supervised learning]
- Missing Data: [Initial assessment of completeness]
```

## Step 5: Use AI Workflow Commands

ARIA uses AI workflow commands to automate the research process. Commands are located in `.claude/commands/academic/`.

### Execute the Workflow

Follow these steps in sequence using Cursor:

1. **Analyze Raw Data**

   In the Cursor chat, type `/` and select `raw-data-analysis.md`

   This analyzes your raw data and creates `docs/02-raw-data-analysis.md`

2. **Preprocess Data**

   Type `/` and select `preprocess.md`

   Creates preprocessing plan and processes data

3. **Design Research Plan**

   Type `/` and select `research-plan.md`

   Develops comprehensive research methodology

4. **Implement Code**

   Type `/` and select `code-implementation.md`

   Generates necessary Python modules in `src/`

5. **Run Experiments**

   Type `/` and select `run-experiments.md`

   Executes the experiment pipeline

6. **Analyze Results**

   Type `/` and select `experiment-analysis.md`

   Analyzes outputs and creates reports

7. **Generate Academic Paper**

   Type `/` and select `research-report.md`

   Creates publication-ready manuscript

8. **Deploy Model (Optional)**

   Type `/` and select `gradio-app.md`

   Creates interactive web interface for your model

## Step 6: Code Quality Checks

After implementing code, ensure quality by running:

```bash
# Type checking
mypy src/

# Code style check
ruff check src/

# Format code
ruff format src/
```

## Step 7: Version Control

Use the intelligent Git commit command:

Type `/` in Cursor chat and select `git-commit.md`

This automatically creates structured commits and can batch large changes.

## Quick Example: Iris Dataset Classification

Here's a complete example using the classic Iris dataset:

1. **Prepare data**:

   ```bash
   # Download Iris dataset to data/raw/
   python -c "
   from sklearn.datasets import load_iris
   import pandas as pd
   iris = load_iris()
   df = pd.DataFrame(iris.data, columns=iris.feature_names)
   df['target'] = iris.target
   df.to_csv('data/raw/iris.csv', index=False)
   "
   ```

2. **Create project description**:

   ```bash
   cat > docs/01-basic-information.md << 'EOF'
   # Project: Iris Species Classification

   ## Objectives
   - Build a classifier to identify iris species
   - Compare multiple ML algorithms

   ## Data Overview
   - Classic Iris dataset
   - 150 samples, 4 features
   - 3 target classes

   ## Research Questions
   1. Which features are most important for classification?
   2. What's the best performing algorithm?

   ## Expected Outcomes
   - Trained classifier with >95% accuracy
   - Feature importance analysis
   EOF
   ```

3. **Run AI workflow in Cursor**:
   Open Cursor and execute commands in sequence by typing `/` in chat:
   - Select `raw-data-analysis.md`
   - Select `preprocess.md`
   - Select `research-plan.md`
   - Select `code-implementation.md`
   - Select `run-experiments.md`
   - Select `experiment-analysis.md`
   - Select `research-report.md`

## Troubleshooting

### Tool Installation Issues

1. **Git not recognized**:
   - Windows: Restart your terminal after installation, or add Git to PATH manually
   - Verify with: `git --version`

2. **Python not found**:
   - Windows: Reinstall Python and check "Add Python to PATH"
   - macOS/Linux: Try `python3` instead of `python`
   - Verify with: `python --version` or `python3 --version`

3. **UV not found**:
   - Close and reopen your terminal after installation
   - Check if UV is in PATH: `echo $PATH` (macOS/Linux) or `echo %PATH%` (Windows)
   - Try reinstalling: [UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)

4. **Permission denied errors**:
   - macOS/Linux: You may need to use `sudo` for system-wide installations
   - Windows: Run PowerShell or Command Prompt as Administrator

### Common Runtime Issues

1. **Import errors**: Ensure all dependencies are installed and virtual environment is activated

   ```bash
   # Activate virtual environment first
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows

   # Then sync dependencies
   uv sync
   ```

2. **AI commands not found**:
   - Make sure you're using Cursor
   - Verify commands exist in `.claude/commands/academic/`
   - In Cursor chat, type `/` to see available commands

3. **Data not found**: Verify data is in `data/raw/` directory

   ```bash
   ls data/raw/  # macOS/Linux
   dir data\raw  # Windows
   ```

4. **Memory issues**: For large datasets, consider:
   - Sampling your data initially
   - Using chunked processing
   - Increasing system memory
   - Using a machine with more RAM

5. **Virtual environment not activating**:
   - Make sure you're in the project root directory
   - Try creating a new virtual environment: `uv venv --python 3.12`
   - On Windows, you may need to enable script execution:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```

### Getting Help

- Check existing issues: [GitHub Issues](https://github.com/Biaoo/aria/issues)
- Create a new issue with:
  - Error message
  - Steps to reproduce
  - Your environment details

## Next Steps

After completing your first analysis:

1. **Customize the workflow**: Modify commands in `.claude/commands/` for your specific needs
2. **Add custom modules**: Create specialized functions in `src/`
3. **Extend visualizations**: Add custom plots in `src/visualization.py`
4. **Share your results**: Deploy your model with Gradio or create a dashboard

## Tips for Success

1. **Start small**: Test with a subset of your data first
2. **Document everything**: Keep `docs/01-basic-information.md` updated
3. **Use version control**: Commit frequently using `/` command to select `git-commit.md`
4. **Check outputs**: Review generated documentation before proceeding
5. **Iterate**: The workflow is flexible - repeat steps as needed

## Additional Resources

- [ARIA Documentation](./README.md)
- [Claude AI Documentation](https://docs.anthropic.com)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

Ready to start? Place your data in `data/raw/`, open Cursor, type `/` in chat and select `raw-data-analysis.md` to begin!
