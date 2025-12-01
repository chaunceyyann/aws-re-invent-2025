# Workflows

## Active Workflows

### `pr-checks.yaml`
Triggers on pull requests to `main` or `dev` branches.

**What it does:**
- Runs pre-commit checks (formatting, linting, validation)
- Runs terraform linting with tflint
- Posts PR status comment with check results

### `python-ci.yaml`
Triggers on push/PR to `main` or `develop` branches - runs Python testing and linting across multiple Python versions.

**What it does:**
- Tests against Python 3.8, 3.9, 3.10, and 3.11
- Installs dependencies from `requirements.txt` and `setup.py` files in `./app`
- Lints code with flake8 (error checking + complexity analysis)
- Runs unit tests (files matching `*test*.py` in `tests/` directories or `test_*.py`)
- Runs integration tests (files matching `*integration*test*.py`)
- Executes pytest with coverage reporting for each app directory
- Generates XML coverage reports
