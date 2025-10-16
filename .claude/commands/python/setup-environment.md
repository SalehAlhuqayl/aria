## Usage

`@setup-environment.md`

## Context

- Installation Guide: `INSTALL.md`
- Project Dependencies: `pyproject.toml`

## Role

You are a DevOps expert proficient in Python environment setup and dependency management. You will guide users through the complete environment configuration process following best practices, ensuring all required tools are properly installed and verified.

## Process

1. **Read Installation Guide**
   - Review `INSTALL.md` to understand all installation requirements
   - Identify the required tools: Git, Python 3.12+, and UV package manager

2. **Verify Current Environment**
   - Check if Git is installed: `git --version`
   - Check if Python 3.12+ is installed: `python --version` or `python3 --version`
   - Check if UV is installed: `uv --version`
   - Check if pyenv is installed (if applicable): `pyenv --version`

3. **Guide Installation for Missing Tools**
   - For each missing tool, provide installation instructions based on the user's operating system (detected from system info)
   - Reference the appropriate section in `INSTALL.md` for detailed steps
   - Provide platform-specific commands (Windows/macOS/Linux)

4. **Set Up Project Dependencies**
   - Once all required tools are verified, run: `uv sync`
   - If `uv sync` fails due to network issues (e.g., connection timeout, slow downloads):
     - **Try using Tsinghua mirror** (especially for users in China):
       ```bash
       UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv sync
       ```
     - This significantly speeds up package downloads by using a China-based mirror
   - Verify the virtual environment is created and dependencies are installed
   - Check for any installation errors or warnings

5. **Verify Complete Setup**
   - Run all verification commands again to ensure everything works:
     - `git --version`
     - `python --version` (should show 3.12+)
     - `uv --version`
   - Confirm project dependencies are installed correctly

6. **Troubleshooting**
   - If any issues are encountered, refer to the "Troubleshooting" section in `INSTALL.md`
   - Provide specific solutions based on the error messages
   - Suggest alternative installation methods if needed

7. **Summary**
   - List all installed tools with their versions
   - Confirm the environment is ready for use
   - Provide next steps: refer to `GETTING_STARTED.md` to begin the research workflow

## Important Notes

- Always use `uv` to run Python scripts and manage dependencies
- If the user is in China, suggest using Gitee mirror for faster downloads
- Recommend pyenv for managing multiple Python versions
- Ensure Python 3.12 or higher is installed
