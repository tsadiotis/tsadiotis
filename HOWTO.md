# How to Use This Starter Repo in a CI/CD Lab

This guide is written as a companion for a live teaching session.

## 1) What you are showcasing

This repo lets you teach a simple but realistic path:

**edit -> test locally -> push -> CI runs -> merge -> deploy static site**

That is enough to introduce the core industry ideas without drowning students in platform details.

## 2) Tools used

### CI tool: GitHub Actions
Use this to teach workflow files, triggers, jobs, steps, runners, artifacts, and logs.

### Deployment tool: GitHub Pages
Use this to teach static deployment, branch-based releases, and the idea that deployment can be automated from the same repo.

## 3) Suggested classroom flow

### Before class
1. Create a public GitHub repo.
   - Enter ```username.github.io``` as the repository name. Replace ```username``` with your GitHub username. For example, if your username is ```ninja-terminator```, the repository name should be ```ninja-terminator.github.io```.
   - read: https://docs.github.com/en/pages/quickstart
2. Push this starter repo to it.
3. Go to **Settings -> Pages** and make sure GitHub Pages is configured to use **GitHub Actions** as the source.
4. Open the repo in GitHub and keep these tabs ready:
   - Code
   - Actions
   - Settings -> Pages
   - the eventual Pages URL

### In class

#### Part A: local dev
Run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```

Explain:
- local test feedback
- reproducibility
- "works on my machine" is not enough

#### Part B: pipeline anatomy
Open `.github/workflows/ci.yml`.
Walk through:
- `on:` trigger
- `jobs:`
- `runs-on:` runner
- `steps:`
- artifact upload

#### Part C: make CI fail on purpose
Edit one test to make it fail, or change a function incorrectly.
Commit and push.
Then show:
- workflow run
- failing job
- logs
- where the failure happened

#### Part D: fix and re-run
Fix the code.
Push again.
Show the green build.

#### Part E: deployment
Open `.github/workflows/pages.yml`.
Explain that deployment is also "just another automated workflow".
Push a small change to `site/index.html`.
Show the Pages deployment run.
Refresh the deployed website.

## 4) Industry terms to explain while teaching

### CI
Continuous Integration. Code changes trigger automated validation.

### CD
Continuous Delivery or Continuous Deployment. Teams use the same initials for two slightly different ideas:
- **delivery** = always ready to release
- **deployment** = actually released automatically

### Workflow
The full automation file.

### Job
A group of steps that runs on one runner.

### Step
One action or shell command inside a job.

### Runner
The machine executing the job.

### Artifact
A saved output from a workflow, such as test results or a built package.

### Build
Anything that transforms source code into a checked or packaged output.

### Deploy
Make the software available in an environment such as staging or production.

### Environment
A target context like dev, staging, or production.

### Branch protection
A rule that prevents merging unless checks pass.

## 5) Useful slang to decode for students

- **green build**: the pipeline passed
- **red build**: the pipeline failed
- **busted build**: someone broke CI
- **ship it**: release or deploy it
- **works on my machine**: local success does not guarantee shared reproducibility
- **flake / flaky test**: a test that fails inconsistently
- **mainline**: the main branch
- **merge gate**: conditions that must pass before merge

## 6) Where to extend this repo later

After the basic lab works, you can extend it with:
- matrix builds across Python versions
- coverage reporting
- dependency caching
- packaging to a release artifact
- container builds
- PR-only checks
- manual approval before deployment

## 7) Suggested talking points for the next lab on agents

Once students understand the pipeline, the AI/agents lab can ask:
- can an agent explain a failed CI run?
- can it generate tests before a PR?
- can it draft a PR description from a diff?
- can it update a workflow safely?

That makes the AI lab feel grounded instead of magical.
