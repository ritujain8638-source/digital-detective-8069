# Mission 1 — Know your computer

## 1. Task / objective
Explain how a computer receives input, processes information, produces output, and stores results using the **IPOS** (Input, Processing, Output, Storage) model. Identify and classify everyday hardware and software components (operating system, application, and utility software), and analyze three embedded/everyday computer systems outside of laptops and phones.

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Typing a study note in a text editor (VS Code) and saving the file to disk.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | I press keys on the keyboard to type characters and press `Cmd + S` (or click Save with the trackpad) to save the document. | Keyboard and trackpad / mouse |
| **Processing** | The processor decodes the keystroke signals into character codes, updates the document buffer in memory, and prepares the file data for writing. | CPU (Apple Silicon processor) and RAM (working memory) |
| **Output** | Each typed letter appears immediately on the display inside the editor window, and the status bar shows that the file has been saved. | Built-in screen / display panel and GPU |
| **Storage** | The completed `.md` text file is written permanently to the solid-state drive so it remains available even after the laptop is powered off. | Internal SSD (Solid-State Drive) |

**How the activity moves from input to output and storage:**
When I press a key on the keyboard (**Input**), an electrical signal is sent to the computer. The operating system and CPU (**Processing**) translate that signal into a character stored temporarily in fast volatile memory (RAM) and instruct the graphics system to draw the character on the screen (**Output**) so I get instant visual feedback. Because RAM clears when the power turns off, pressing Save triggers the CPU and operating system to write those bytes from RAM onto the non-volatile SSD (**Storage**) as a permanent file.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Keyboard** | Hardware | Not applicable | Used to enter text and keyboard shortcuts into the computer. |
| **Trackpad / Mouse** | Hardware | Not applicable | Controls the on-screen pointer to select, click, and scroll through items. |
| **CPU (Apple M-series chip)** | Hardware | Not applicable | Executes program instructions and performs calculations. |
| **Solid-State Drive (SSD)** | Hardware | Not applicable | Stores the operating system, applications, and user files persistently. |
| **Built-in Display / Monitor** | Hardware | Not applicable | Visually displays text, graphics, and the user interface. |
| **macOS** | Software | Operating system software | Manages hardware resources (CPU, memory, disk) and provides a platform for applications to run. |
| **Visual Studio Code (VS Code)** | Software | Application software | Helps me write, edit, and organize code and Markdown documentation. |
| **Web Browser (Chrome / Safari)** | Software | Application software | Allows me to access websites, read documentation, and interact with GitHub. |
| **Activity Monitor** | Software | Utility software | Monitors CPU load, memory usage, and running processes to help diagnose performance issues. |
| **Disk Utility / Time Machine** | Software | Utility software | Manages storage volumes, checks disk health, and maintains system backups. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Bank ATM (Automated Teller Machine)** | Allows customers to withdraw cash and check account balances without a human teller. | Debit card chip reader and PIN keypad entry. | Dispensed currency notes and printed paper receipt / screen balance display. |
| **Metro Ticket Vending Machine** | Issues travel tokens or recharges smart cards for public transit commuters. | Touchscreen station selection and UPI QR / cash payment sensor. | Printed QR paper ticket or updated smart card balance message on screen. |
| **Smart Washing Machine** | Automates washing, rinsing, and spinning clothes based on fabric and load weight. | Control dial / button selection and internal water-level / weight sensors. | Motor rotation of the drum, water valve operation, and LED cycle countdown timer + completion buzzer. |

## 3. Commands / tools used
- **Text Editor (VS Code):** Used to write and format the Markdown tables for Tasks 1.1, 1.2, and 1.3.
- **Git (`git status`, `git add`, `git commit`):** Used to verify modified files, stage only Mission 1 changes, and commit the completed mission.

## 4. My understanding
Every computing action—no matter how complex—follows the **IPOS cycle**: taking raw **Input**, transforming or acting on it in **Processing** (using CPU and RAM), presenting results via **Output**, and keeping data long-term in **Storage**.

I also learned the clear boundary between **hardware** (physical parts you can touch, such as the SSD, CPU, keyboard, and screen) and **software** (the instructions that tell hardware what to do). Within software, **operating system software** (like macOS) acts as the manager of the whole machine, **application software** (like VS Code or a browser) lets the user accomplish direct tasks, and **utility software** (like Activity Monitor or Disk Utility) helps maintain, inspect, and protect the system. Finally, computers are not just laptops and phones—embedded systems like ATMs and ticket machines use the exact same IPOS principles with specialized sensors and actuators.

## 5. Difficulties faced
At first, it was slightly tricky to distinguish between **Processing** memory (RAM) and **Storage** (SSD) when tracing a document edit, since both hold data.

## 6. How I resolved them
I reviewed how data behaves while typing versus saving: while I am typing a line, the unsaved letters live in RAM (part of the active processing workspace), and only when the file is saved are they written permanently to the SSD (storage).

## 7. Evidence / files
- [`mission-01-computer-basics/README.md`](./README.md) — Contains the completed IPOS table (Task 1.1), Hardware & Software classification table (Task 1.2), and Everyday Computer Systems table (Task 1.3).

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Status:** Committed on `main` branch and ready/verified for GitHub push.
