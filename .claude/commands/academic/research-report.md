## Usage

`@research-report.md`

## Context

- Basic information: `docs/01-basic-information.md`
- All analysis documents in `docs/`
- Experiment report: `docs/09-experiment-report.md`
- Output results in `output/`

## Style

- High-impact journal format (Nature/Science style)
- Concise, data-driven narrative
- Emphasis on methodology rigor and result significance

## Process

1. Read all project documentation and experimental outputs:
   - Basic information (`docs/01-basic-information.md`)
   - Data analysis (`docs/02-raw-data-analysis.md`, `docs/04-processed-data-analysis.md`)
   - Research plan (`docs/05-research-plan.md`)
   - Experiment report (`docs/09-experiment-report.md`)
   - All numerical results and figures in `data/output/`

2. Generate manuscript in `docs/10-manuscript.md` following Nature/Science format:
   - **Title**: Concise, impactful statement of main finding
   - **Author Information**: Placeholder for authors and affiliations
   - **Abstract** (150-200 words):
     - Context and knowledge gap
     - Main methodology innovation
     - Key quantitative results
     - Significance and implications
   - **Main Text** (3000-4000 words):
     - Opening paragraph: Problem significance and research gap
     - Results presentation with key figures
     - Method highlights and innovations
     - Discussion of implications
   - **Methods** (detailed section):
     - Data acquisition and characteristics
     - Preprocessing pipeline
     - Model architecture/analysis approach
     - Statistical methods
     - Computational details
     - Code availability statement
   - **References**: Don't include references in the manuscript.

3. Create publication-ready figures:
   - Main figures (3-4): Core results with high visual impact
   - Extended data figures: Supporting analyses
   - Follow journal figure guidelines (size, resolution, labeling)

4. Generate Supplementary Information in `docs/10-manuscript-supplement.md`:
   - Extended methods
   - Additional results
   - Detailed statistical analyses
   - Data tables
   - Algorithm descriptions

5. Quality checks:
   - Verify all statistical claims
   - Ensure figure-text consistency
   - Check quantitative accuracy
   - Validate method reproducibility

6. Create submission materials:
   - Cover letter draft in `docs/10-cover-letter.md`
   - Highlights/significance statement
   - Data availability statement