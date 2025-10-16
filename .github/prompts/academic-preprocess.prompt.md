## Usage

`@preprocess.md`

## Context

- Basic information of the project: `docs/01-basic-information.md`
- Raw data stored in `data/raw/`
- Raw data analysis: `docs/02-raw-data-analysis.md`

## Tools

- Use tools like `cat`|`head`|`tail`|`grep`|`pandas`|`json` to read data.

## Process

1. Read the basic information of the project: `docs/01-basic-information.md`
2. Read the raw data analysis: `docs/02-raw-data-analysis.md`
3. According to the basic information of the project and the raw data analysis, design the data preprocessing plan to make the data suitable and standardized for further analysis, write the data preprocessing plan to `docs/03-preprocess-plan.md`.
4. According to the data preprocessing plan, write necessary scripts for data preprocessing to `scripts/`, the processed data should be stored in `data/processed/`.
5. Run the scripts to preprocess the data.
6. Read and analyze the processed data and write the analysis results to `docs/04-processed-data-analysis.md`. The analysis results should be concise and clear, including specific data types, data field types, quantity, storage files, data characteristics, etc.
7. Update the basic information of the project: `docs/01-basic-information.md` to include the data preprocessing plan and the processed data analysis results in response to the changes.