# Mission 0 — Create your GitHub workspace

## 1. Task / objective
Create a properly named project folder and Git repository (`digital-detective-8069` using the last four digits of my USN), verify that Python 3 and Git are installed on my computer, build the required directory and file structure for all nine missions, and prepare the root and Mission 0 documentation.

## 2. Work completed
- Verified the installed versions of Python 3 and Git in Terminal:
  - **Python version:** `Python 3.13.15`
  - **Git version:** `git version 2.56.0`
- Created the local repository folder named `digital-detective-8069`.
- Initialized Git inside `digital-detective-8069` with `main` as the default branch.
- Created all required mission folders and initial files:
  - `README.md` (Root overview and mission index)
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md`
  - `mission-05-numbers-data/number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/` (with `evidence/mission-00-tools.txt`)

## 3. Commands / tools used
- **`python3 --version`**: Checked that Python 3 is installed and displayed its version number (`3.13.15`).
- **`git --version`**: Checked that Git is installed and displayed its version number (`2.56.0`).
- **`mkdir -p`**: Created the root project folder, the nine mission folders, and the `evidence/` directory.
- **`touch`**: Created the initial empty Markdown files and `number_converter.py` placeholder.
- **`git init -b main`**: Initialized a new Git repository with `main` as the primary branch.
- **`git add` & `git commit`**: Staged the workspace structure and recorded the initial setup commit.

## 4. My understanding
A **repository** (or "repo") is a project folder tracked by a version control system like Git. In addition to holding normal files and subfolders, it keeps a complete timeline of commits so that I can inspect changes over time, revert mistakes, and publish my work to an online host like GitHub.

Organizing the folder structure by mission (`mission-00-setup` through `mission-08-final-report`) keeps each topic isolated and easy to navigate. Instead of dumping scripts, notes, and outputs into one crowded folder, anyone reviewing the repository can open a specific mission folder and immediately see the README and code that belong to that task.

## 5. Difficulties faced
When creating empty folders in Git (such as `evidence/`), I noticed that Git does not track completely empty directories unless there is at least one file inside them.

## 6. How I resolved them
I saved the privacy-safe version check output into `evidence/mission-00-tools.txt` and created the required `README.md` files inside each mission folder so Git could stage and track the entire directory tree right from Mission 0.

## 7. Evidence / files
- [`README.md`](../README.md) — Root overview and mission index.
- [`mission-00-setup/README.md`](./README.md) — Setup documentation and tool version check.
- [`evidence/mission-00-tools.txt`](../evidence/mission-00-tools.txt) — Saved output of `python3 --version` and `git --version`.

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Status:** Committed on `main` branch and ready/verified for GitHub push.
