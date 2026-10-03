# CASPROTTO — COMBINATORICS CALCULATOR

An exact-integer terminal calculator for basic combinatorics.

**Version:** 1.0.0
**Author:** Casprotto

---

## Overview

**Casprotto Combinatorics Calculator** is a Python terminal application designed to calculate common combinatorial quantities using exact integer arithmetic.

The calculator provides seven operations, including formulas with and without repetition.

It also includes an integrated **WHAT? help system** that explains the meaning of the variables, the mathematical operation, and a practical example for each calculation.

---

## Features

* Exact integer calculations
* Seven combinatorial operations
* Support for very large integer results
* Input validation
* Mathematical validation
* Integrated `WHAT?` help system
* `ESC` navigation
* Terminal-based graphical interface using colored panels and boxes
* Dedicated result screens showing:

  * operation
  * formula
  * calculation
  * result
* Graceful handling of `Ctrl+C` and `EOF`
* No external Python packages required

---

## Available Operations

### 1. Factorial

Calculates the factorial of `N`.

**Formula:**

```text
N!
```

Example:

```text
5! = 120
```

---

### 2. Permutation

Arranges all `N` distinct elements in every possible order.

**Formula:**

```text
N!
```

Example:

```text
3! = 6
```

---

### 3. Arrangement

Selects `K` distinct elements from `N` elements where order matters.

**Formula:**

```text
N! / (N-K)!
```

Example:

```text
N = 5
K = 2

5! / (5-2)! = 20
```

---

### 4. Combination

Selects `K` distinct elements from `N` elements where order does not matter.

**Formula:**

```text
N! / (K! * (N-K)!)
```

Example:

```text
N = 5
K = 2

5! / (2! * 3!) = 10
```

---

### 5. Permutation with Repetition

Arranges all elements when some elements are identical.

**Formula:**

```text
N! / (n1! * n2! * ...)
```

Example:

```text
N = 5
Repetition counts = 3,2

5! / (3! * 2!) = 10
```

The repetition counts must add up to `N`.

---

### 6. Arrangement with Repetition

Creates ordered groups of `K` elements chosen from `N` available elements, with repetition allowed.

**Formula:**

```text
N^K
```

Example:

```text
N = 3
K = 2

3^2 = 9
```

---

### 7. Combination with Repetition

Selects `K` elements from `N` available elements where order does not matter and repetition is allowed.

**Formula:**

```text
(N+K-1)! / (K! * (N-1)!)
```

Example:

```text
N = 3
K = 2

(3+2-1)! / (2! * (3-1)!) = 6
```

---

## Requirements

### Running the Python source

The calculator requires:

* Python 3
* A terminal capable of displaying ANSI escape sequences

The program uses only Python's standard library:

```text
os
sys
textwrap
```

No external packages are required.

---

## How to Use

Start the program and choose an operation from the main menu.

```text
[F]   Factorial
[P]   Permutation
[A]   Arrangement
[C]   Combination

[PR]  Permutation with repetition
[AR]  Arrangement with repetition
[CR]  Combination with repetition

[H]   About
[Q]   Quit
```

Follow the prompts to enter the required values.

For example, an arrangement requires:

```text
N
K
```

while a permutation with repetition requires:

```text
N
repetition counts
```

---

## WHAT? Help System

Inside a calculation, type:

```text
WHAT
```

to open the integrated help system.

Depending on the operation, the help system can explain:

* `N`
* `K`
* repetition counts
* the operation itself
* an example

The help system can be left at any time using:

```text
ESC
```

---

## Input Validation

The calculator validates both the format and the mathematical validity of the input.

### Format validation

Invalid inputs such as:

```text
abc
1.5
```

are rejected when an integer is required.

For repetition counts, the program expects comma-separated integers, for example:

```text
3,2
```

---

### Mathematical validation

The calculator checks conditions such as:

* `N` cannot be negative for factorial-based operations
* `K` cannot be negative
* `K` cannot be greater than `N` where applicable
* `N` must be greater than zero for operations requiring `N-1`
* repetition counts must be greater than zero
* repetition counts must add up exactly to `N`

Invalid mathematical inputs are rejected without terminating the program.

---

## Exact Integer Arithmetic

All calculations are performed using Python integers.

The calculator does not use floating-point arithmetic for the combinatorial results.

This means the results are exact integers rather than approximations.

Python's large-integer string conversion limit is disabled when supported by the installed Python version, allowing very large exact results to be displayed.

---

## Navigation

The calculator uses simple keyboard commands.

### Main menu

```text
Q
```

Quit the program.

```text
ESC
```

Also exits from the main menu.

### Calculation screens

```text
WHAT
```

Open help.

```text
ESC
```

Return to the main menu.

---

## Error Handling

The program handles invalid input through dedicated error screens.

Examples include:

```text
FORMAT ERROR
```

for invalid input formats, and:

```text
MATHEMATICAL ERROR
```

for mathematically invalid values.

The program also handles:

```text
Ctrl+C
```

and end-of-file input without displaying a Python traceback.

---

## Running from Python

Run the source file from a terminal with:

```bash
python Casprotto_Combinatorics_Calculator_1.0.0.py
```

Depending on the system, you may need to use:

```bash
python3 Casprotto_Combinatorics_Calculator_1.0.0.py
```

---

## Building the Executable

The project can be packaged as a standalone Windows executable using **PyInstaller**.

Example:

```bash
pyinstaller --onefile --icon=casprotto.ico --name "Casprotto Combinatorics Calculator" Casprotto_Combinatorics_Calculator_1.0.0.py
```

The application is a terminal program, so a console window should remain enabled.

The resulting executable will be placed in:

```text
dist/
```

---

## Project Structure

A release package can contain:

```text
Casprotto Combinatorics Calculator/
│
├── Casprotto_Combinatorics_Calculator_1.0.0.py
├── README.md
├── casprotto.ico
└── dist/
    └── Casprotto Combinatorics Calculator.exe
```

The `.exe` is the standalone Windows build.

The `.py` file contains the original Python source code.

---

## Version

### 1.0.0

Initial release.

The application currently includes:

* 7 combinatorial calculations
* exact integer arithmetic
* input validation
* mathematical validation
* integrated WHAT? help
* terminal interface
* error handling
* About screen

---

## Author

Created by **Casprotto**.

**Casprotto — Combinatorics Calculator 1.0.0**
