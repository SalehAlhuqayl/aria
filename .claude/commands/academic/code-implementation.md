## Usage

`@code-implementation.md`

## Context

- Research plan: `docs/05-research-plan.md`
- Processed data stored in `data/processed/`
- Source code directory: `src/`

## Tools

- Python with scientific libraries (pandas, numpy, scikit-learn, etc.)
- Code quality tools: mypy, ruff

## Process

1. Read the research plan: `docs/05-research-plan.md`
2. Implement code modules based on the research plan:
   - Create `src/feature_engineering.py` for feature engineering
   - Create `src/models.py` for analysis methods/models
   - Create `src/evaluation.py` for evaluation metrics
   - Create `src/visualization.py` for data visualization
   - Create `src/pipeline.py` for experiment pipeline
   - Create `src/utils.py` for utility functions
3. Ensure proper code structure with:
   - Type hints for all functions
   - Docstrings for all modules, classes, and functions
   - Error handling and logging
   - Configuration management
4. Run code quality checks:
   - `mypy src/` for type checking
   - `ruff check src/` for code style
   - `ruff format src/` for code formatting
5. Create `scripts/run_experiment.py` as the main execution script(including training, evaluation, visualization,etc.).
6. Write implementation documentation to `docs/06-implementation-docs.md` including:
   - Module descriptions and dependencies
   - Key algorithms and methods
   - Configuration parameters
   - Code Structure
7. Write execution instructions to `docs/07-execution-instructions.md` including:
   - Environment setup
   - Script usage
   - Parameter configurations
   - Expected outputs

## Note

- If extra dependencies are needed, ALWAYS use UV to add the dependencies.
- Use UV to run python scripts.
- In the output directory, not only the final results but also all essential intermediate information (such as results from baseline models, training process logs, and visualization figures) must be saved.
