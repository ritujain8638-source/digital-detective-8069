# The Digital Detective — Mini System Report (`digital-detective-8069`)

Welcome to my **Digital Detective** independent learning assignment repository (`digital-detective-8069`). This project is a hands-on exploration of how my computer works—covering hardware and software fundamentals, Terminal file management, operating system processes and permissions, program translation, number systems and text encoding, Git/GitHub version control, and computer networking.

> **Privacy Note:** In compliance with the assignment guidelines, all personal and network identifiers (such as computer usernames, email addresses, device serial numbers, Wi-Fi names, and private/local IP addresses) have been omitted or replaced with `[redacted]`.

---

## Workflow & Commit Policy

Every mission (`Mission 0` through `Mission 8`) was completed in strict sequence, documented inside its own mission folder using the standardized 8-section README format, and committed separately with a clear, descriptive commit message before moving on to the next mission.

---

## Mission Index

| Mission | Focus Area | Mission Documentation & Code | Status |
| :--- | :--- | :--- | :--- |
| **Mission 0** | Repository and workspace setup | [mission-00-setup/README.md](./mission-00-setup/README.md) | Completed |
| **Mission 1** | Computer fundamentals and IPOS | [mission-01-computer-basics/README.md](./mission-01-computer-basics/README.md) | Completed |
| **Mission 2** | Terminal and file management | [mission-02-terminal/README.md](./mission-02-terminal/README.md) | Completed |
| **Mission 3** | Operating system, processes and permissions | [mission-03-operating-system/README.md](./mission-03-operating-system/README.md) | Completed |
| **Mission 4** | How programs run | [mission-04-programs/README.md](./mission-04-programs/README.md) · [hello.py](./mission-04-programs/hello.py) | Completed |
| **Mission 5** | Number systems, Python and text encoding | [mission-05-numbers-data/README.md](./mission-05-numbers-data/README.md) · [number_converter.py](./mission-05-numbers-data/number_converter.py) | Completed |
| **Mission 6** | Git, GitHub, branches and Pull Requests | [mission-06-git-github/README.md](./mission-06-git-github/README.md) | Completed |
| **Mission 7** | Computer networks | [mission-07-networking/README.md](./mission-07-networking/README.md) | Completed |
| **Mission 8** | Final review and submission | [mission-08-final-report/README.md](./mission-08-final-report/README.md) | Completed |
| **Evidence** | Privacy-safe command outputs | [evidence/](./evidence/) | Completed |

---

## Topics Explored

- **Computer Fundamentals & IPOS:** Tracing Input, Processing, Output, and Storage; classifying hardware vs. operating system, application, and utility software; analyzing embedded computer systems.
- **Terminal & CLI Operations:** Navigating directories (`pwd`, `ls`, `cd`), safely creating/copying/renaming files (`mkdir`, `touch`, `cp`, `mv`, `cat`), appending vs. overwriting (`>>` vs. `>`), using flags (`-lah`) and pipes (`|`), and inspecting Homebrew (`brew`).
- **Operating Systems:** Inspecting macOS system info (`sw_vers`, `uname`), disk usage (`df -h`), running processes and Process IDs (`PID`), absolute vs. relative paths, Unix file permissions (`rwx`), and the six core OS responsibilities.
- **Program Execution:** Writing and executing a Python script (`hello.py`) and comparing compilers with interpreters.
- **Number Systems & Text Encoding:** Converting between decimal (base 10), binary (base 2), and hexadecimal (base 16) by hand and in Python; building `number_converter.py`; understanding ASCII and UTF-8 character encoding.
- **Git & GitHub Collaboration:** Staging (`git add`), committing (`git commit`), viewing history (`git log`), working with feature branches (`update-about`), and using Pull Requests.
- **Computer Networking:** Understanding `LAN`, `MAN`, `WAN`, `DNS`, routers, protocols, packet switching, and the client-server model; testing connectivity (`ping`) and DNS resolution (`nslookup`).

---

## How to Run the Python Programs

### 1. Run the Number Converter (`Mission 5`)
From the root of the repository (or inside `mission-05-numbers-data/`), run:
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
When prompted (`Enter a positive decimal integer:`), type any positive whole number (for example `13`, `25`, or `255`) and press **Enter** to see its binary and hexadecimal representations.

### 2. Run the Hello Program (`Mission 4`)
```bash
cd mission-04-programs
python3 hello.py
```

---

## My Learning

Through this assignment, I built a connected picture of how a computer works from bottom to top:
1. **Command-Line & OS Confidence:** I can navigate folders, inspect permissions (`rwx`), check storage and running processes (`PID`), and safely manipulate files in Terminal using flags (`-lah`) and pipes (`|`).
2. **How Programs & Data Work Internally:** I understand how high-level Python code is executed by an interpreter, how decimal numbers translate into binary (`0b`) and hexadecimal (`0x`), and how text characters are stored as numeric codes using ASCII and UTF-8.
3. **Structured Version Control & Networking:** Staging and committing each mission separately—and isolating updates on branches like `update-about`—keeps a clean, reversible history of my work, while DNS, routers, and protocols allow my local machine to communicate reliably with remote servers like GitHub.

4. **Privacy-Safe Technical Documentation:** Redacting sensitive system details while preserving clear command evidence makes a public repository both safe and reproducible.
