# coursera-ds-capstone

Scaffold for a root-level Python package managed with `uv`.

## Layout

- `src/coursera_ds_capstone/`: importable package code
- `tests/`: pytest-based tests
- `pyproject.toml`: project metadata and tooling configuration

## Common commands

```bash
uv sync
uv run pytest
uv run coursera-ds-capstone
```

## Git workflow

### Create a new feature branch locally and push it to remote

```bash
git status
git checkout main
git pull origin main
git checkout -b feature/<your-branch-name>

# make your changes, then:
git status
git add .
git commit -m "Add my new feature"
git push -u origin feature/<your-branch-name>
```

### Start from the latest remote code, create a new branch, and modify files

```bash
git fetch origin
git checkout main
git pull origin main
git checkout -b feature/my-next-change

# edit files, then:
git status
git add .
git commit -m "Update project files"
git push -u origin feature/my-next-change
```

## Notebooks

This workspace includes lab notebooks in `notebooks/`.

- `notebooks/jupyter-labs-spacex-data-collection-api-v2.ipynb`
- `notebooks/jupyter-labs-webscraping.ipynb`

### Notebook setup

1. Run `uv sync` from the project root to install the notebook dependencies.
2. Open a notebook in VS Code.
3. Select the `coursera-ds-capstone` Python 3.11.13 kernel.
4. Run the cells from top to bottom.

### What is already installed

The project environment includes the libraries used by the notebooks:

- `beautifulsoup4`
- `ipykernel`
- `numpy`
- `pandas`
- `requests`

If VS Code does not show the kernel automatically, use the notebook kernel picker and choose the `coursera-ds-capstone` environment created by `uv`.
