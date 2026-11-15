# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers manually between decimal (base 10), binary (base 2), and hexadecimal (base 16) showing full step-by-step working, verify those conversions in Python, build and test an interactive `number_converter.py` program with at least three inputs, and explain how computers represent text using ASCII and UTF-8 encoding.

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | **Repeated division by 2:**<br>`13 ÷ 2 = 6` remainder **`1`**<br>`6 ÷ 2 = 3` remainder **`0`**<br>`3 ÷ 2 = 1` remainder **`1`**<br>`1 ÷ 2 = 0` remainder **`1`**<br>Reading remainders from bottom to top (or `8 + 4 + 0 + 1`): **`1101`** |
| **Convert decimal 25 to binary.** | **Repeated division by 2:**<br>`25 ÷ 2 = 12` remainder **`1`**<br>`12 ÷ 2 = 6` remainder **`0`**<br>`6 ÷ 2 = 3` remainder **`0`**<br>`3 ÷ 2 = 1` remainder **`1`**<br>`1 ÷ 2 = 0` remainder **`1`**<br>Reading remainders from bottom to top (or `16 + 8 + 0 + 0 + 1`): **`11001`** |
| **Convert binary 1010 to decimal.** | **Place values (`2³`, `2²`, `2¹`, `2⁰`):**<br>`(1 × 8) + (0 × 4) + (1 × 2) + (0 × 1) = 8 + 0 + 2 + 0` = **`10`** |
| **Convert binary 1101 to decimal.** | **Place values (`2³`, `2²`, `2¹`, `2⁰`):**<br>`(1 × 8) + (1 × 4) + (0 × 2) + (1 × 1) = 8 + 4 + 0 + 1` = **`13`** |
| **Convert hexadecimal A to decimal.** | In base 16, `A` stands for `10`:<br>`10 × 16⁰ = 10 × 1` = **`10`** |
| **Convert hexadecimal 1F to decimal.** | **Place values (`16¹`, `16⁰`), where `F = 15`:**<br>`(1 × 16) + (15 × 1) = 16 + 15` = **`31`** |
| **Convert binary 1111 to hexadecimal.** | **Convert 4-bit nibble to decimal first, then hex:**<br>`(1 × 8) + (1 × 4) + (1 × 2) + (1 × 1) = 15` in decimal.<br>In hexadecimal, `15` is represented by **`F`**. |

---

### Task 5.2 — Verify using Python

| Manual Conversion | Python Expression Tested | Python Output | Matches Manual Calculation? |
| :--- | :--- | :--- | :--- |
| Decimal `13` → Binary `1101` | `bin(13)` | `'0b1101'` | Yes (`0b` is Python's binary prefix) |
| Decimal `25` → Binary `11001` | `bin(25)` | `'0b11001'` | Yes |
| Binary `1010` → Decimal `10` | `int('1010', 2)` | `10` | Yes |
| Binary `1101` → Decimal `13` | `int('1101', 2)` | `13` | Yes |
| Hex `A` → Decimal `10` | `int('A', 16)` | `10` | Yes |
| Hex `1F` → Decimal `31` | `int('1F', 16)` | `31` | Yes |
| Binary `1111` → Hex `F` | `hex(int('1111', 2))` | `'0xf'` | Yes (`0x` is Python's hex prefix) |

---

### Task 5.3 — Build a small number converter
I created [`mission-05-numbers-data/number_converter.py`](./number_converter.py) which prompts the user for a decimal integer and converts it to both binary and hexadecimal.

#### Test results with three positive numbers:

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **`13`** | `0b1101` (`1101`) | `0xd` (`D`) |
| **`25`** | `0b11001` (`11001`) | `0x19` (`19`) |
| **`255`** | `0b11111111` (`11111111`) | `0xff` (`FF`) |

#### What the conversion functions do:
- **`input()` and `int()`:** `input()` reads the text typed by the user in Terminal as a string, and `int()` converts that string of digits into an actual base-10 integer that Python can do math on.
- **`bin(n)`:** Takes an integer `n` and returns its base-2 (binary) representation as a string prefixed with `'0b'` (for example, `bin(25)` returns `'0b11001'`).
- **`hex(n)`:** Takes an integer `n` and returns its base-16 (hexadecimal) representation as a string prefixed with `'0x'` (for example, `hex(255)` returns `'0xff'`).

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase **`A`** = **`65`** (binary `01000001`)
  - Lowercase **`a`** = **`97`** (binary `01100001`)
- **Why a computer needs an encoding standard to store text:**
  Computer memory and storage hardware can only store binary numbers (`0`s and `1`s), not visual shapes of letters. A character-encoding standard like ASCII or UTF-8 provides a shared lookup rulebook that maps every letter, digit, and symbol to a specific number so any computer can save and display text consistently without garbling it.
- **Example of a character not part of basic ASCII:**
  The Indian Rupee sign **`₹`** (or a Hindi Devanagari character like **`अ`**, or the Diwali diya emoji **`🪔`**) is not part of basic 7-bit ASCII (which only covers 128 basic English characters and control codes), so it requires **UTF-8 / Unicode**.

## 3. Commands / tools used
- **`python3` (interactive REPL):** Used to test `bin()`, `hex()`, `int(value, base)`, and `ord()` interactively.
- **`python3 mission-05-numbers-data/number_converter.py`**: Ran the converter script from Terminal with test values `13`, `25`, and `255`.
- **`input()`, `int()`, `bin()`, `hex()`**: Built-in Python functions used inside `number_converter.py`.

## 4. My understanding
At the hardware level, everything inside a computer—numbers, text, images, and instructions—is stored as bits (`0` and `1`) grouped into 8-bit bytes. Because long strings of binary bits are tedious for humans to read, programmers often use **hexadecimal** (base 16), where a single hex digit (`0`–`F`) neatly represents exactly 4 binary bits (one nibble), and two hex digits (`00`–`FF`, or `0`–`255`) represent one full byte. Similarly, text is stored by mapping each character to a numeric code point via **ASCII** (for basic English text) or **UTF-8** (for all world languages and symbols).

## 5. Difficulties faced
When I first tested `bin(13)` and `hex(255)` in Python, the returned strings started with `0b` and `0x` (`'0b1101'` and `'0xff'`), which looked slightly different from my handwritten answers (`1101` and `FF`).

## 6. How I resolved them
I learned that `0b` and `0x` are standard prefixes Python uses to make it clear whether a string is binary or hexadecimal. In `number_converter.py`, I displayed both the standard Python output (`0b...` / `0x...`) and the clean digits (`[2:]`) so both formats are easy to read.

## 7. Evidence / files
- [`mission-05-numbers-data/number_converter.py`](./number_converter.py) — Working Python number converter program.
- [`mission-05-numbers-data/README.md`](./README.md) — Manual conversions with step-by-step working, Python verification table, converter test table, and text encoding answers.
- [`evidence/mission-05-converter-output.txt`](../evidence/mission-05-converter-output.txt) — Saved Terminal output from interactive Python checks and running `number_converter.py`.

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Status:** Committed on `main` branch and ready/verified for GitHub push.
