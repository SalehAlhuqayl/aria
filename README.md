
# ARIA - Automated Research Intelligence Assistant

**🚀 Transform months of research into minutes of insight**

English | [中文](./README_zh.md)

ARIA is an automated research assistant framework for scientific data analysis, visualization, and report generation.

## Project Structure

```
aria/
├── .claude/commands/           # Claude AI command files
│   ├── academic/               # Academic workflow commands
│   └── git/                    # Git operation commands
├── data/
│   ├── raw/                   # Original data
│   └── processed/              # Preprocessed data
│   └── output/                 # Experiment outputs
│       ├── models/             # Trained models
│       ├── results/            # Experimental results
│       ├── figures/            # Visualization charts
│       └── logs/               # Execution logs
├── docs/                       # Project documentation
├── src/                        # Source code
├── scripts/                    # Execution scripts
```

## Workflow

### 1. Data Preparation
- Place raw data in the `data/raw/` folder
- Manually create `docs/01-basic-information.md` to describe project background, objectives, and data overview

### 2. Data Analysis
- **Raw Data Analysis**: Use `@raw-data-analysis.md` command to analyze raw data, generating `docs/02-raw-data-analysis.md`
- **Data Preprocessing**: Use `@preprocess.md` command to design preprocessing plan (`docs/03-preprocess-plan.md`), execute preprocessing, analyze processed data (`docs/04-processed-data-analysis.md`)

### 3. Research Design
- **Research Plan**: Use `@research-plan.md` command to develop research plan including feature engineering, model selection, evaluation metrics, generating `docs/05-research-plan.md`

### 4. Code Implementation
- **Code Development**: Use `@code-implementation.md` command to implement research plan, creating necessary Python modules
- Generate `docs/06-implementation-docs.md` (implementation documentation) and `docs/07-execution-instructions.md` (execution guide)
- Code quality check: Use mypy and ruff to ensure code quality

### 5. Experiment Execution
- **Run Experiments**: Use `@run-experiments.md` command to execute experiment scripts
- Outputs saved to corresponding subfolders in `output/` directory

### 6. Results Analysis
- **Results Analysis**: Use `@experiment-analysis.md` command to analyze experiment outputs
- Generate individual analyses in `docs/08-experiment-results/` directory
- Generate `docs/09-experiment-report.md` comprehensive experiment report

### 7. Paper Writing
- **Academic Paper**: Use `@research-report.md` command to generate high-impact journal format paper
- Generate `docs/10-manuscript.md` (main text), `docs/10-manuscript-supplement.md` (supplementary materials), `docs/10-cover-letter.md` (cover letter)

### 8. Model Deployment (Optional)
- **Gradio Interface**: If models are trained, use `@gradio-app.md` command to create model inference interface
- Generate `docs/11-model-deployment-guide.md` deployment guide

## Claude AI Commands

### Academic Commands

All academic command files are located in `.claude/commands/academic/` directory:

- `@raw-data-analysis.md` - Analyze raw data
- `@preprocess.md` - Data preprocessing
- `@research-plan.md` - Research plan design
- `@code-implementation.md` - Code implementation
- `@run-experiments.md` - Experiment execution
- `@experiment-analysis.md` - Results analysis
- `@research-report.md` - Academic paper generation
- `@gradio-app.md` - Model deployment interface

### Git Commands

Git command files are located in `.claude/commands/git/` directory:

- `@git-commit.md` - Intelligent Git commits
  - Automatically creates structured commit messages
  - When there are many modified files, automatically commits in batches (max 10 files per commit)
  - Generates meaningful commit descriptions based on code changes

## Quick Start

1. **Prepare Data**: Place raw data in `data/raw/`
2. **Create Project Description**: Write `docs/01-basic-information.md`
3. **Execute Workflow**: Use Claude AI to execute commands in sequence
4. **Version Control**: Use `@git-commit.md` for intelligent commits

## Dependency Management

Using UV for Python dependency management:

```bash
uv add <package-name>  # Add new dependency
uv sync                # Synchronize dependencies
```

## Code Quality

- Type checking: `mypy src/`
- Code style: `ruff check src/`
- Code formatting: `ruff format src/`

## Features

- 📊 **Data-Driven**: Complete workflow from raw data to academic paper
- 🤖 **AI-Assisted**: Claude AI commands automate each research phase
- 📝 **Academic Standards**: Generate Nature/Science standard papers
- 🎯 **Quality Assurance**: Integrated code quality checking tools
- 🚀 **Model Deployment**: Support for Gradio interface rapid deployment
- 📦 **Version Control**: Intelligent Git commit management

## TODO / Roadmap

### Near-term Goals
- [ ] **AI Client Compatibility Testing**
  - Claude Code (currently supported)
  - Cursor AI adaptation
  - GitHub Copilot integration
  - OpenAI CodeX compatibility
  - Other AI coding assistants

- [ ] **Full Workflow Automation**
  - Design autonomous research agent
  - Implement end-to-end pipeline automation
  - Add checkpoint and recovery mechanisms
  - Parallel experiment execution support

- [ ] **Enhanced Features**
  - Multi-modal data support (images, audio, video)
  - Distributed computing integration
  - Real-time collaboration features
  - Cloud deployment options (AWS, GCP, Azure)

### Long-term Vision
- [ ] **Framework Extensions**
  - Plugin system for custom workflows
  - Template library for common research types
  - Integration with popular ML frameworks (PyTorch, TensorFlow, JAX)
  - Support for more academic journal formats

- [ ] **Quality Improvements**
  - Automated testing framework
  - Performance benchmarking
  - Documentation generation
  - Interactive tutorials

- [ ] **Community Features**
  - Research template marketplace
  - Workflow sharing platform
  - Collaborative research tools
  - Pre-built analysis modules

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

## Contact

For questions, suggestions, or collaboration opportunities:

- **GitHub Issues**: [Create an issue](https://github.com/Biaoo/aria/issues)
- **Email**: `biao00luo@gmail.com`
- **Project**: [ARIA on GitHub](https://github.com/Biaoo/aria)