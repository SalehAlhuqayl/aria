# CLAUDE.md

This file provides guidance to AI assistants when working with code in this repository.

## Project Introduction

ARIA - Automated Research Intelligence Assistant is a rapid scaffold for scientific data analysis, visualization, and reporting. It follows a structured workflow from raw data analysis to academic paper generation.

## Project Structure

```
aria/
├── .claude/commands/academic/  # AI command files for each workflow stage
├── data/
│   ├── raw/                   # Original data files
│   └── processed/              # Preprocessed data ready for analysis
│   └── output/                 # Experiment outputs
│       ├── models/             # Trained models
│       ├── results/            # Experimental results
│       ├── figures/            # Visualization charts
│       └── logs/               # Execution logs
├── docs/                       # All project documentation (numbered sequentially)
│   ├── 01-basic-information.md        # Project foundation (manually created)
│   ├── 02-raw-data-analysis.md        # Raw data exploration
│   ├── 03-preprocess-plan.md          # Preprocessing strategy
│   ├── 04-processed-data-analysis.md  # Processed data characteristics
│   ├── 05-research-plan.md            # Research design
│   ├── 06-implementation-docs.md      # Code documentation
│   ├── 07-execution-instructions.md   # Execution guide
│   ├── 08-experiment-results/         # Individual result analyses
│   ├── 09-experiment-report.md        # Consolidated analysis
│   ├── 10-manuscript.md                # Academic paper
│   ├── 10-manuscript-supplement.md    # Supplementary materials
│   ├── 10-cover-letter.md             # Journal submission letter
│   └── 11-model-deployment-guide.md   # Gradio deployment guide
├── src/                        # Source code modules
│   ├── feature_engineering.py
│   ├── models.py
│   ├── evaluation.py
│   ├── visualization.py
│   ├── pipeline.py
│   ├── utils.py
│   └── gradio_app.py          # (if models exist)
├── scripts/                    # Execution scripts
│   ├── run_experiment.py
│   └── launch_app.py          # (if models exist)
```

## Workflow Commands

Use these commands in sequence to complete the research workflow:

1. `@raw-data-analysis.md` - Analyze raw data in `data/raw/`
2. `@preprocess.md` - Design and execute data preprocessing
3. `@research-plan.md` - Create comprehensive research plan
4. `@code-implementation.md` - Implement analysis code with quality checks
5. `@run-experiments.md` - Execute experiment pipeline
6. `@experiment-analysis.md` - Analyze and document results
7. `@research-report.md` - Generate Nature/Science style manuscript
8. `@gradio-app.md` - Create model deployment interface (if applicable)

## Code Quality Standards

- **Type Hints**: All functions must have type annotations
- **Docstrings**: All modules, classes, and functions need comprehensive docstrings
- **Testing**: Run `mypy src/` for type checking
- **Linting**: Run `ruff check src/` and `ruff format src/`
- **Error Handling**: Implement proper exception handling and logging

## Dependencies

Dependencies are managed using UV:
- Add dependencies: `uv add <package-name>`
- Sync environment: `uv sync`
- Lock file: `uv.lock`

Common dependencies for this project:
- Data processing: pandas, numpy
- Machine learning: scikit-learn, xgboost, lightgbm
- Deep learning: torch, tensorflow (as needed)
- Visualization: matplotlib, seaborn, plotly
- Web interface: gradio
- Quality tools: mypy, ruff

## Run Scripts

- ALWAYS use uv to run python scripts.

## Important Guidelines

### File Creation
- NEVER create files unless explicitly necessary for the task
- ALWAYS prefer editing existing files over creating new ones
- Documentation files should only be created as specified in the workflow

### Documentation
- Follow the numbered documentation structure in `docs/`
- Keep documentation concise, clear, and data-driven
- Focus on reproducibility and methodology

### Academic Writing
- Manuscripts should follow Nature/Science format
- Emphasize methodology rigor and statistical significance
- Include proper supplementary materials
- Generate publication-ready figures

### Model Deployment
- Only create Gradio apps when trained models exist
- Focus on user-friendly interfaces for model inference
- Include proper input validation and error handling

## Git Workflow

- DO NOT commit changes unless explicitly requested by the user
- When committing, include clear, descriptive messages
- Follow the repository's commit message conventions