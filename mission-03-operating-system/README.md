# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the operating system environment on my computer using Terminal, inspect active user account identity, storage space, and running processes, compare absolute and relative paths, analyze file permission flags (`r`, `w`, `x`), and explain the six core responsibilities of an operating system.

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details (`sw_vers`, `uname -m`)** | Identifies the operating system name, version number, build, and processor architecture. | Running `macOS 27.2.1` (Darwin kernel) on `arm64` (Apple Silicon architecture). |
| **Current account identity (`whoami`)** | Shows which user account is currently logged into the active Terminal session. | Returned my active local user account (`[redacted]`). |
| **Available and used storage (`df -h /`)** | Reports total disk capacity, used space, and remaining free space in human-readable units (`Gi`). | Root SSD volume (`/dev/disk3s1s1`) has `460Gi` total size, `13Gi` system snapshot used, and `213Gi` available free space. |
| **System activity snapshot (`top -l 1` / `ps`)** | Provides a live summary of running processes, CPU load, and memory usage. | Multiple background daemons and user applications are active, with low idle CPU usage and normal memory pressure. |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is an active instance of a computer program that is currently loaded into memory and being executed by the operating system. While a program on disk is just passive code, it becomes one or more processes as soon as it starts running.
- **What does the PID column represent?**
  **PID** stands for **Process Identifier**. It is a unique number assigned by the operating system to every running process so the OS (and user tools like Activity Monitor or `ps`) can track, schedule, or stop that exact process without confusing it with others.
- **Two examples of processes running on my computer:**
  1. **`Terminal` / `zsh`** — My interactive command-line shell and Terminal application window.
  2. **`WindowServer` (or `Visual Studio Code` / `Google Chrome`)** — `WindowServer` is a background system process that draws all application windows on the macOS screen, while `Visual Studio Code` is an active user application process.

---

### Task 3.3 — Understand paths and permissions

#### Absolute Path vs. Relative Path
- **Absolute path:** Always starts from the root directory (`/`) and specifies the complete location of a file or folder regardless of where you currently are in Terminal.
  - *Example from my repository:* `/Users/[redacted]/digital-detective-8069/mission-03-operating-system/README.md`
- **Relative path:** Starts from your *current working directory* and describes how to reach the target from where you already stand (using folder names, `.` for current directory, or `..` for parent directory).
  - *Example from my repository (when standing in `digital-detective-8069`):* `mission-03-operating-system/README.md` (or `../mission-02-terminal/README.md` when standing inside `mission-03-operating-system`).

#### File Permissions Analysis
I inspected `mission-02-terminal/terminal-practice/notes.txt` using `ls -l`:
```text
-rw-r--r--  1 [redacted]  staff  108 Nov 15 17:47 mission-02-terminal/terminal-practice/notes.txt
```
- The first character `-` indicates a regular file (whereas `d` indicates a directory).
- The next three characters (`rw-`) represent the **owner** permissions:
  - **`r` (Read):** Present — the owner **can read** the contents of `notes.txt`.
  - **`w` (Write):** Present — the owner **can edit/modify** `notes.txt`.
  - **`-` (Execute absent):** The `x` bit is off — the owner **cannot execute** `notes.txt` directly as a program or script (which makes sense because it is a plain text note, not an executable script).

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **`r` — Read** | Allows a file's contents to be read. | Opening and viewing a text file with `cat` or a text editor. |
| **`w` — Write** | Allows a file to be changed or saved over. | Editing and saving changes to `notes.txt`. |
| **`x` — Execute** | Allows a file to be run as a program; on a directory, allows entering/traversing it. | Running an executable shell script or `cd`-ing into a folder. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Decides which running programs get CPU time, switches rapidly between tasks (multitasking), and starts or terminates processes safely. | Running a web browser, VS Code, and Terminal smoothly at the same time without one freezing the others. |
| **Memory management** | Allocates portions of RAM to each running program, prevents programs from reading each other's memory, and reclaims RAM when an app closes. | Giving VS Code the RAM it needs to open a project and freeing that memory when I quit VS Code. |
| **Device management** | Communicates with hardware peripherals through device drivers so applications do not need custom hardware code. | Translating trackpad gestures, keyboard presses, or audio output to headphones automatically. |
| **File management** | Organizes data on the storage drive into a hierarchy of folders and files, tracking filenames, sizes, and locations. | Saving `README.md` inside `mission-03-operating-system/` on the APFS file system. |
| **User interface / shell** | Provides a visual desktop (GUI) and a command-line interpreter (shell) so humans can interact with the computer. | Using macOS Finder windows (GUI) or typing commands into the `zsh` Terminal shell (CLI). |
| **Security and permissions** | Protects the system by requiring user authentication and enforcing read/write/execute rules on files and folders. | Preventing a normal user command from deleting protected macOS system files without administrator permission. |

## 3. Commands / tools used
- **`sw_vers` & `uname -srpm`**: Checked the macOS version, Darwin kernel release, and `arm64` processor type.
- **`whoami`**: Checked the currently active user account name.
- **`df -h /`**: Checked disk space usage on the main volume in human-readable gigabytes (`Gi`).
- **`ps` / Activity Monitor**: Viewed active processes and their unique Process Identifiers (`PID`).
- **`cd` & `pwd`**: Navigated between the assignment root folder and `mission-03-operating-system` to observe path changes.
- **`ls -l`**: Viewed the permission string (`-rw-r--r--`) for `notes.txt`.

## 4. My understanding
The operating system sits between physical hardware and user programs, acting as both a coordinator and a traffic controller. Without the OS managing **processes** and **memory**, two apps could overwrite each other's data or hog the CPU. I also gained a practical understanding of **paths** (knowing when to use a short relative path inside my repo vs. an absolute path from `/`) and **Unix file permissions** (`rwx`), which let the OS enforce security right at the file level.

## 5. Difficulties faced
When reading the output of `df -h /` on macOS, the total size minus used space did not appear to equal the available space directly at first glance.

## 6. How I resolved them
I learned that modern macOS uses APFS (Apple File System), where the system snapshot volume (`/dev/disk3s1s1`) shares a single storage container pool with the user data volume, so `Avail` (`213Gi`) reflects the free space left across the entire shared container.

## 7. Evidence / files
- [`mission-03-operating-system/README.md`](./README.md) — Contains the OS exploration table, process notes, path/permission analysis, and OS responsibilities table.
- [`evidence/mission-03-os-snapshot.txt`](../evidence/mission-03-os-snapshot.txt) — Privacy-safe output of `sw_vers`, `uname`, `whoami`, `df -h /`, `ps`, and `ls -l`.

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Status:** Committed on `main` branch and ready/verified for GitHub push.
