## Usage

`@run-experiments.md`

## Context

- Execution instructions: `docs/07-execution-instructions.md`
- Main experiment script: `scripts/run_experiment.py`
- Processed data in `data/processed/`
- Output directory: `output/`

## Process

1. Read the execution instructions: `docs/07-execution-instructions.md`
2. Verify environment setup and dependencies
3. Create output directory structure:
   - `output/models/` for trained models
   - `output/results/` for numerical results
   - `output/figures/` for visualizations
   - `output/logs/` for execution logs
4. Execute the experiment pipeline:
   ```bash
   python scripts/run_experiment.py
   ```
5. Monitor execution progress and capture any errors
6. Verify all expected outputs are generated:
   - Model files
   - Result metrics (CSV/JSON)
   - Visualization figures
   - Execution logs
7. Create execution summary in `output/execution_summary.txt` including:
   - Start and end times
   - Parameters used
   - Files generated
   - Any warnings or errors
8. Validate output integrity and completeness