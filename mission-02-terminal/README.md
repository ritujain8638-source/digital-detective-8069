# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Practice essential command-line interface (CLI) operations inside the assignment repository, safely create and modify practice text files without losing existing data, understand how command flags (`-l`, `-a`, `-h`) and pipes (`|`) work, and explore how a package manager (Homebrew) manages software on macOS.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full path of the folder I am currently working inside. | Displayed `/Users/[redacted]/.../digital-detective-8069/mission-02-terminal`. |
| **Directory listing (`ls`)** | Lists the visible files and folders in the current working directory. | Showed the names `README.md` and `terminal-practice` in a simple list. |
| **Detailed listing (`ls -l`)** | Shows a multi-column listing with permissions, owner, file size, modification date, and name. | Each item appeared on its own row starting with permission codes like `-rw-r--r--` or `drwxr-xr-x`. |
| **Change directory (`cd ..`)** | Moves the active Terminal location one level up to the parent folder. | My working directory changed from `mission-02-terminal` up to the root `digital-detective-8069` folder (confirmed with `pwd`). |
| **Create directory (`mkdir terminal-practice`)** | Creates a new empty subfolder with the specified name. | A new folder named `terminal-practice` appeared when I ran `ls`. |
| **Create empty file (`touch practice.txt`)** | Creates a new empty (`0` byte) file if it does not exist, or updates its timestamp. | Created `practice.txt` inside `terminal-practice/` with size `0B`. |
| **Copy file (`cp practice.txt practice_copy.txt`)** | Duplicates the source file into a second file with a new name. | Both `practice.txt` and `practice_copy.txt` existed side by side in the folder. |
| **Move / rename file (`mv practice_copy.txt practice_renamed.txt`)** | Renames a file in place or moves it to another folder path. | `practice_copy.txt` disappeared and became `practice_renamed.txt`. |
| **Display file contents (`cat notes.txt`)** | Reads a file and prints its text contents directly in the Terminal window. | Printed both lines of text that I added to `notes.txt` directly to the screen. |

---

### Task 2.2 — Practise file changes safely
Inside `mission-02-terminal/terminal-practice/`, I created `notes.txt`, wrote a first line using `>`, appended a second line using `>>`, verified both lines with `cat notes.txt`, copied the file to `notes_backup.txt`, and renamed the backup to `notes_backup_v1.txt`.

#### Answers to Task 2.2 questions:
1. **What is the difference between replacing a file's contents and adding text to the end?**
   Replacing contents (using a single redirect `>`) wipes out everything currently inside the file and writes only the new text. Adding text to the end (appending with `>>`) preserves all existing lines and writes the new line at the bottom of the file.
2. **What is the difference between copying a file and moving a file?**
   Copying (`cp`) creates an independent duplicate so both the original file and the new copy exist at the same time. Moving (`mv`) relocates the file (or renames it), leaving only one file at the destination.
3. **What information does the current-directory display provide?**
   The `pwd` (Print Working Directory) command shows the exact full hierarchy of folders leading from the system root (`/`) to the directory where the shell is currently operating, preventing me from running file commands in the wrong folder.
4. **Why is a directory-listing operation useful?**
   Running `ls` lets me confirm which files and folders actually exist in my current location, check exact filenames and extensions before editing or deleting, and (with flags) inspect file sizes, timestamps, and permissions.

---

### Task 2.3 — Understand flags and pipes
- **Comparing `ls` vs. `ls -lah`:**
  - A plain `ls` only showed the names of non-hidden files (`README.md`, `terminal-practice`).
  - Adding the flags `-l` (long format), `-a` (all files, including hidden dotfiles), and `-h` (human-readable sizes) changed the output completely: it revealed hidden entries like `.` (current folder) and `..` (parent folder), displayed permissions (`drwxr-xr-x`), and formatted byte counts into readable units like `128B` and `5.2K`.
- **Using a pipe (`ls -lah | head -n 5`):**
  - The **pipe symbol (`|`)** connects two commands by taking the text output produced by the command on the left and feeding it directly as the input to the command on the right.
  - **Left side (`ls -lah`):** Generates the full, detailed directory listing of all files.
  - **Right side (`head -n 5`):** Filters that incoming stream and prints only the first 5 lines to the screen, which is very helpful when a folder has hundreds of items.

---

### Task 2.4 — Understand package managers
- **Observation on my Mac:** Homebrew is installed (`Homebrew 7.0.12`). Running `brew --version` confirmed the version, and `brew list` displayed managed command-line packages such as `btop`, `ffmpeg`, `gh`, and `gettext`.
- **Why package managers are useful:**
  A package manager automates finding, downloading, installing, updating, and removing software from trusted repositories using simple Terminal commands. Instead of manually searching websites for installers and hunting down missing libraries, a package manager like Homebrew automatically installs all required dependencies in the right folders and lets you update every tool at once.

## 3. Commands / tools used
- **`pwd`**: Displayed the current working directory path.
- **`ls` / `ls -l` / `ls -lah`**: Listed directory contents in basic, long, and hidden + human-readable formats.
- **`cd`**: Changed the active working directory (`cd ..` to move up one level).
- **`mkdir`**: Created the `terminal-practice` folder.
- **`touch`**: Created an empty text file (`practice.txt`).
- **`echo` with `>` and `>>`**: Wrote initial text (`>`) and appended a second line (`>>`) into `notes.txt`.
- **`cp`**: Copied `practice.txt` and `notes.txt` to backup files.
- **`mv`**: Renamed the copied files (`practice_renamed.txt` and `notes_backup_v1.txt`).
- **`cat`**: Displayed the full contents of `notes.txt`.
- **`head -n 5` with `|` (pipe)**: Displayed only the first 5 lines of output from `ls -lah` and `brew list`.
- **`brew --version` & `brew list`**: Checked the installed Homebrew version and listed managed packages without installing or removing anything.

## 4. My understanding
The Terminal gives direct, precise control over the file system. Every command has a base action (like `ls`, `cp`, or `mv`), and **flags** (like `-l`, `-a`, `-h`) customize how that command behaves. I also learned how important it is to know the difference between `>` (which overwrites a file) and `>>` (which safely appends to it), and how **pipes (`|`)** let small commands work together like building blocks by passing output from one tool into another.

## 5. Difficulties faced
When using `ls -l`, the raw file sizes are printed in bytes, which can be hard to read quickly for larger files, and normal `ls` hides files that start with a dot (`.`).

## 6. How I resolved them
I combined the `-a` (all files) and `-h` (human-readable) flags with `-l` as `ls -lah`, which neatly displayed hidden entries alongside readable units like `B` and `K`.

## 7. Evidence / files
- [`mission-02-terminal/README.md`](./README.md) — Command reference table, safe file-change answers, flags/pipes explanation, and package manager notes.
- [`mission-02-terminal/terminal-practice/practice.txt`](./terminal-practice/practice.txt) — Empty practice file from Task 2.1.
- [`mission-02-terminal/terminal-practice/practice_renamed.txt`](./terminal-practice/practice_renamed.txt) — Copied and renamed practice file from Task 2.1.
- [`mission-02-terminal/terminal-practice/notes.txt`](./terminal-practice/notes.txt) — Two-line text file created in Task 2.2.
- [`mission-02-terminal/terminal-practice/notes_backup_v1.txt`](./terminal-practice/notes_backup_v1.txt) — Renamed backup copy of `notes.txt` from Task 2.2.
- [`evidence/mission-02-terminal-output.txt`](../evidence/mission-02-terminal-output.txt) — Privacy-safe log of the Terminal commands and outputs.

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Status:** Committed on `main` branch and ready/verified for GitHub push.
