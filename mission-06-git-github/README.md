# Mission 6 — Git and GitHub

## 1. Task / objective
Practice the core Git version control workflow (`status`, `add`, `commit`, `log`), explain the difference between staging and committing, create and publish a feature branch named `update-about` to add a `"My Learning"` section to the root `README.md`, understand how Pull Requests enable team collaboration, and build a nine-command Git glossary in my own words.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Shows which branch I am currently on, which files have been modified or created, and which changes are staged vs. unstaged. |
| **Stage selected changes (`git add <file>`)** | Moves specific modified or new files into the staging area so they are prepared to be included in the next commit snapshot. |
| **Create a commit (`git commit -m "..."`)** | Saves a permanent, timestamped snapshot of all currently staged changes in the local repository history with a descriptive message. |
| **View commit history (`git log --oneline`)** | Lists past commits in reverse chronological order, showing each commit's unique hash identifier and commit message. |

#### Difference between staging (`git add`) and committing (`git commit`):
**Staging (`git add`)** is like placing selected items into a shopping cart or packing box—it lets you choose *which* specific file changes belong together without permanently recording them yet. **Committing (`git commit`)** is like sealing and labeling that box—it takes everything currently in the staging area and records it permanently as a new version snapshot in the repository's history. Having a separate staging step prevents you from accidentally bundling unrelated or unfinished edits into the same commit.

---

### Task 6.2 & Task 6.3 — Create a branch (`update-about`) and Pull Request workflow
1. I created and switched to a new branch named `update-about` using `git checkout -b update-about`.
2. I opened the root [`README.md`](../README.md) and added a `## My Learning` section summarizing three key takeaways from the missions so far.
3. I verified the change with `git status`, staged `README.md` (`git add README.md`), and committed it on `update-about` with the message `"Add My Learning section to root README"`.
4. **Branch & Pull Request Status:** Both `main` and `update-about` are preserved in the repository so the branch history and Pull Request from `update-about` into `main` are visible on GitHub.

#### What a Branch and a Pull Request are, and why they are useful:
- **What is a branch?** A branch is an independent line of development that splits off from the main project (`main`). It lets you work on a new feature, documentation update, or bug fix in isolation without risking breaking the working code on `main`.
- **What is a Pull Request (PR)?** A Pull Request is a formal proposal on GitHub asking to merge the changes from one branch (such as `update-about`) into another branch (such as `main`).
- **Why they are useful for teams:** When multiple people work on the same repository, branches prevent everyone from overwriting each other's files directly on `main`. Pull Requests give teammates and instructors a dedicated place to inspect the exact line-by-line diff, leave review comments, run automated checks, and approve the changes before they are merged into `main`.

---

### Task 6.4 — Git command glossary (one-line explanations in my own words)
1. **Initialise a repository (`git init`):** Turns an ordinary folder into a new Git repository by creating the hidden `.git` tracking directory.
2. **Check status (`git status`):** Displays the current branch name along with any untracked, modified, or staged files in the workspace.
3. **Stage changes (`git add <file>`):** Marks specific file edits to be included in the upcoming commit snapshot.
4. **Commit changes (`git commit -m "message"`):** Permanently records the staged changes into the local repository history with a clear explanation message.
5. **View history (`git log`):** Shows the chronological list of previous commits, including commit hashes, authors, dates, and messages.
6. **Create or list branches (`git branch`):** Lists existing branches in the repository or creates a new branch pointer at the current commit.
7. **Switch branches (`git switch <branch>` / `git checkout <branch>`):** Changes your active working directory from one branch to another.
8. **Publish changes (`git push`):** Uploads your local commits and branches to a remote repository hosted on GitHub.
9. **Retrieve remote changes (`git pull`):** Downloads the latest commits from the remote GitHub repository and merges them into your current local branch.

## 3. Commands / tools used
- **`git status`**: Checked modified and staged files before and after editing `README.md`.
- **`git checkout -b update-about`**: Created and switched to the `update-about` branch in one step.
- **`git add`**: Staged specific mission files (`README.md` and `mission-06-git-github/README.md`).
- **`git commit -m "..."`**: Created dedicated commits for the `update-about` branch and Mission 6 documentation.
- **`git log --oneline --graph --decorate`**: Inspected the commit history and branch structure visually in Terminal.
- **`git merge --no-ff update-about`**: Integrated the `update-about` branch changes while keeping the branch commit history visible.

## 4. My understanding
Git makes experimenting safe because nothing is permanent until committed, and branches like `update-about` let me isolate changes away from `main`. I now understand why professional developers never edit `main` directly: using a feature branch plus a Pull Request creates a clean audit trail showing *what* changed, *why* it changed, and *how* it was reviewed before joining the main codebase.

## 5. Difficulties faced
At first, it was easy to confuse `git add` and `git commit` and wonder why Git needs two steps just to save a change.

## 6. How I resolved them
By practicing `git status` before and after `git add`, I saw how the staging area lets me cherry-pick only the files belonging to the current mission while leaving other files untouched until I am ready for them.

## 7. Evidence / files
- [`mission-06-git-github/README.md`](./README.md) — Git workflow table, staging vs. committing explanation, branch & PR notes, and 9-command Git glossary.
- [`README.md`](../README.md) — Updated root README containing the `## My Learning` section added on the `update-about` branch.
- [`evidence/mission-06-git-log.txt`](../evidence/mission-06-git-log.txt) — Saved output of `git status`, `git branch -a`, and `git log --oneline --graph`.

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Status:** Committed on `main` branch (with `update-about` branch created and tracked) and ready/verified for GitHub push.
