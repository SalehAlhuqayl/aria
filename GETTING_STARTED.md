# Getting Started with ARIA

This guide will walk you through the complete process of using ARIA (Automated Research Intelligence Assistant) from setup to generating your first research report.

## Prerequisites

- Python 3.10 or higher
- Git
- [Claude Code](https://claude.com/product/claude-code) or [Cursor](https://www.cursor.com/)
- UV package manager (recommended) or pip

## Step 1: Fork and Clone the Repository

### Option A: Fork on GitHub (Recommended)

1. Visit [ARIA on GitHub](https://github.com/Biaoo/aria)
2. Click the "Fork" button in the top-right corner
3. Clone your forked repository:

```bash
git clone https://github.com/YOUR_USERNAME/aria.git
cd aria
```

### Option B: Direct Clone

```bash
git clone https://github.com/Biaoo/aria.git
cd aria
```

## Step 2: Set Up Python Environment

See [INSTALL.md](./INSTALL.md) for more details.

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

## Step 5: Use Claude AI Commands

ARIA uses Claude AI commands to automate the research workflow. Commands are located in `.claude/commands/`.

### Execute the Workflow

Follow these steps in sequence using Claude Code:

1. **Analyze Raw Data**

   ```
   @raw-data-analysis.md
   ```

   This analyzes your raw data and creates `docs/02-raw-data-analysis.md`

2. **Preprocess Data**

   ```
   @preprocess.md
   ```

   Creates preprocessing plan and processes data

3. **Design Research Plan**

   ```
   @research-plan.md
   ```

   Develops comprehensive research methodology

4. **Implement Code**

   ```
   @code-implementation.md
   ```

   Generates necessary Python modules in `src/`

5. **Run Experiments**

   ```
   @run-experiments.md
   ```

   Executes the experiment pipeline

6. **Analyze Results**

   ```
   @experiment-analysis.md
   ```

   Analyzes outputs and creates reports

7. **Generate Academic Paper**

   ```
   @research-report.md
   ```

   Creates publication-ready manuscript

8. **Deploy Model (Optional)**

   ```
   @gradio-app.md
   ```

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

```
@git-commit.md
```

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

3. **Run Claude AI workflow**:
   Open Claude Code and execute commands in sequence:

   ```
   @raw-data-analysis.md
   @preprocess.md
   @research-plan.md
   @code-implementation.md
   @run-experiments.md
   @experiment-analysis.md
   @research-report.md
   ```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure all dependencies are installed

   ```bash
   uv sync  # or pip install -e .
   ```

2. **Claude AI commands not found**: Make sure you're using Claude Code and the commands are in `.claude/commands/`

3. **Data not found**: Verify data is in `data/raw/` directory

4. **Memory issues**: For large datasets, consider:
   - Sampling your data initially
   - Using chunked processing
   - Increasing system memory

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
3. **Use version control**: Commit frequently with `@git-commit.md`
4. **Check outputs**: Review generated documentation before proceeding
5. **Iterate**: The workflow is flexible - repeat steps as needed

## Additional Resources

- [ARIA Documentation](./README.md)
- [Claude AI Documentation](https://docs.anthropic.com)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

Ready to start? Place your data in `data/raw/` and begin with `@raw-data-analysis.md`!
