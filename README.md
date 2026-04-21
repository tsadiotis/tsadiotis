# CI/CD Lab Starter Repo

A tiny Python project you can use to demo:

- local development
- automated tests with GitHub Actions
- linting and formatting checks
- artifact upload
- static deployment to GitHub Pages

## Quick start

```bash
git clone <your-fork-url>
cd cicd-lab-starter
python3 -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest
ruff check .
ruff format --check .
```

## What this repo contains

- `src/calc_service/` - tiny Python package
- `tests/` - pytest tests
- `.github/workflows/ci.yml` - CI pipeline
- `.github/workflows/pages.yml` - Pages deployment pipeline
- `site/` - static site deployed to GitHub Pages
- `HOWTO.md` - companion guide for your lecture/demo

## Demo ideas

1. Push a commit with a broken test and watch CI go red.
2. Fix the bug and watch CI go green.
3. Show the artifact upload step in Actions.
4. Enable GitHub Pages and show the site being deployed automatically.

## Intentional teaching hooks

- The `divide()` function raises a friendly error for division by zero.
- The Pages workflow only deploys on pushes to `main`.
- The CI workflow runs on both `push` and `pull_request`.

## How to use this repo
    - See more details [here](HOWTO.md)