# Mission 4 — How programs run

## 1. Task / objective
Create and run a one-line Python script (`hello.py`) from the Terminal using Python 3, and compare how compilers and interpreters translate human-readable source code into instructions that a computer can execute.

## 2. Work completed

### Task 4.1 — Create and run a Python program
I created `mission-04-programs/hello.py` containing the following single line of Python code:
```python
print("Hello from Python")
```
I then executed it from the Terminal:
```text
$ python3 mission-04-programs/hello.py
Hello from Python
```
The message `Hello from Python` appeared immediately in the Terminal output.

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code into machine code *before* the program is run (ahead-of-time compilation). | Reads, translates, and executes the source code step by step *while* the program is running (at runtime). |
| **Typical output** | Produces a standalone executable file (such as an `.exe` or native binary) or object file. | Does not produce a separate standalone executable file; it directly carries out the program's actions and prints output. |
| **One example** | C / C++ (`clang`, `gcc`) or Rust (`rustc`). | Python (`python3`) or JavaScript (in a browser / Node.js). |
| **One advantage** | Faster runtime execution because the entire program has already been translated into native machine instructions beforehand. | Faster development and testing cycle—you can edit a line of code and run the script immediately without waiting for a separate build step. |

#### Explanation of the difference (in my own words):
As shown in the comparison table, the main difference between a compiler and an interpreter is **when** translation happens and **what** is produced. A **compiler** (like `gcc` or `clang` for C) acts like translating an entire book into another language before handing the finished book to a reader: it converts the whole source file into a standalone machine-code executable ahead of time, which makes the final program run very fast. In contrast, an **interpreter** (like `python3` when running `hello.py`) acts like a live translator who reads and executes the source code statement by statement at runtime without creating a separate binary file. This makes interpreted languages like Python very convenient for quick testing, experimentation, and cross-platform scripting.

## 3. Commands / tools used
- **Text Editor (VS Code):** Created and saved `mission-04-programs/hello.py`.
- **`python3 mission-04-programs/hello.py`**: Invoked the Python 3 interpreter to read and execute `hello.py`.
- **`print()`**: Built-in Python function used inside `hello.py` to output text to the standard output stream in Terminal.

## 4. My understanding
Computers only understand low-level machine instructions (binary `0`s and `1`s), whereas programmers write code in high-level languages like Python or C. To bridge that gap, we rely on either a **compiler** or an **interpreter** (or a combination of both, since CPython internally compiles `.py` source into bytecode before interpreting it on the Python Virtual Machine). Running `python3 hello.py` demonstrated how an interpreter lets me run source code directly on the spot without first generating a separate executable file.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [`mission-04-programs/hello.py`](./hello.py) — Working one-line Python script that prints `"Hello from Python"`.
- [`mission-04-programs/README.md`](./README.md) — Program execution walkthrough and compiler vs. interpreter comparison table.
- [`evidence/mission-04-hello-output.txt`](../evidence/mission-04-hello-output.txt) — Saved Terminal output of running `hello.py`.

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Status:** Committed on `main` branch and ready/verified for GitHub push.
