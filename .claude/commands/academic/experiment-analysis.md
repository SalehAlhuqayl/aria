## Usage

`@experiment-analysis.md`

## Context

- Experiment outputs in `output/`
- Research plan: `docs/05-research-plan.md`

## Tools

- Python for data analysis (pandas, numpy, matplotlib, seaborn)
- Statistical analysis tools

## Process

1. Read all experiment outputs from `output/` directory:
   - Model performance metrics
   - Prediction results
   - Visualization figures
   - Execution logs
2. Analyze each output file and create detailed descriptions:
   - Statistical summaries
   - Performance comparisons
   - Key findings and insights
   - Unexpected results or anomalies
3. Generate additional analysis visualizations if needed:
   - Comparison charts
   - Error analysis plots
   - Feature importance visualizations
4. Write individual analysis for each result file to `docs/08-experiment-results/`:
   - Create one markdown file per output file
   - Include quantitative metrics
   - Provide qualitative interpretation
5. Create comprehensive experiment report in `docs/09-experiment-report.md`:
   - Executive summary
   - Methodology recap
   - Results presentation
   - Statistical analysis
   - Key findings
   - Limitations and future work
6. Generate tables and figures for the report
7. Cross-validate results with research objectives