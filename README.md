# HENNGE Challenge — Sum of Fourth Powers

A Python solution for the HENNGE coding challenge that reads multiple test cases from standard input, filters non-positive integers from each case, raises them to the **4th power**, and outputs the sum.

---

## 📋 Problem Statement

Given **N** test cases, each consisting of:

1. An integer **X** — the expected count of numbers
2. A line of **X** space-separated integers **Yₙ** (where −100 ≤ Yₙ ≤ 100)

For each test case, compute the **sum of Yₙ⁴** for all **non-positive** values of Yₙ (i.e., Yₙ ≤ 0). Positive values are excluded from the calculation.

If the actual count of numbers on the line does not match **X**, output **-1** for that case.

### Constraints

| Parameter | Range            |
|-----------|------------------|
| N         | 1 ≤ N ≤ 100      |
| X         | 1 ≤ X ≤ 100      |
| Yₙ        | −100 ≤ Yₙ ≤ 100  |

> The final output for each test case is guaranteed to fit within a 32-bit signed integer.

---

## 🧪 Example

### Input

```
2
4
3 -1 1 10
5
9 -5 -5 -10 10
```

### Output

```
1
11250
```

### Explanation

| Case | Numbers          | Non-positive | Computation                            | Result  |
|------|------------------|-------------|----------------------------------------|---------|
| 1    | 3, -1, 1, 10     | -1          | (-1)⁴ = 1                              | **1**   |
| 2    | 9, -5, -5, -10, 10 | -5, -5, -10 | (-5)⁴ + (-5)⁴ + (-10)⁴ = 625 + 625 + 10000 | **11250** |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+** (no external dependencies required)

### Running the Solution

```bash
python main.py < test_input.txt
```

Or provide input interactively via stdin:

```bash
python main.py
```

---

## 📁 Project Structure

```
HENNGE challenge/
├── main.py                   # Main solution
├── test_input.txt            # Sample input file
├── test_solution.py          # Core test suite (14 tests)
├── test_all.py               # Comprehensive test suite (21 tests)
├── test_extra_edge_cases.py  # Additional edge case tests (12 tests)
└── README.md                 # This file
```

---

## 🧩 How It Works

The solution is structured using a **functional programming** style:

1. **`read_line()`** — Reads the next non-empty line from stdin (recursively skips blank lines).
2. **`power_of_four(x)`** — Returns `x⁴`.
3. **`sum_negatives_and_zero(numbers)`** — Filters non-positive integers, raises each to the 4th power, and sums them using `reduce`.
4. **`process_case()`** — Reads a single test case (X + numbers), validates the count, and returns the result (or `-1` on mismatch).
5. **`process_all(n, results)`** — Recursively processes all N test cases.
6. **`main()`** — Entry point that reads N and orchestrates execution.

---

## ✅ Running Tests

Three test scripts are provided, each runnable with:

```bash
# Core tests (14 cases)
python test_solution.py

# Comprehensive tests (21 cases)
python test_all.py

# Extra edge case tests (12 cases)
python test_extra_edge_cases.py
```

### Test Coverage

| Category              | Examples                                          |
|-----------------------|---------------------------------------------------|
| **Sample input**      | Challenge-provided example                        |
| **All positive**      | All values excluded → `0`                         |
| **All negative**      | All values included                               |
| **All zeros**         | `0⁴ = 0` for each                                |
| **Mixed values**      | Combination of positive, negative, and zero       |
| **Boundary values**   | Yₙ = ±100, X = 100, N = 100                      |
| **X mismatch**        | Fewer or more numbers than X → `-1`               |
| **Multiple cases**    | Verifies independent processing of each case      |
| **Edge cases**        | `-0` parsing, large sums, consecutive mismatches  |

---

## 📄 License

This project is for educational and challenge-submission purposes.
