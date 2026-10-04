# Session 01 — Typed Calculator

A beginner-friendly, src-based Python project with four typed functions:
`add`, `subtract`, `multiply`, and `divide`, plus the stretch operations
`percentage_change` and `compound_growth`. The implementation is in
`src/calculator_project/calculator.py` (inside this project folder).

## Retrieval check

- Inputs: core operations receive two numbers; stretch operations receive old/new values or a principal, rate, and number of periods.
- Success: each function returns the expected result, and all checks pass.
- Boundaries: zero must work for multiplication, but a zero divisor must raise an error.

## Initialization

This project was created using:

```sh
uv init --app --package --python 3.9 --vcs none calculator-project
```

The generated `pyproject.toml`, `.python-version`, `README.md`, and
`src/calculator_project/__init__.py` are included. The README and package entry
point were then updated, and the calculator and dependency lockfile were added.
`--vcs none` skips Git metadata, which is not needed for submission.

## Setup and usage

Install uv if needed: https://docs.astral.sh/uv/getting-started/installation/

Unzip the submission, open a terminal in `calculator-project`, and run:

```sh
uv sync --locked
uv run calculator-project
```

`uv sync` creates a local `.venv` and installs this package from `src`.
`uv.lock` records the project dependency resolution. No third-party runtime
libraries are required. The environment is recreated locally rather than included
in the ZIP. The selected Python version is recorded in `.python-version`.

You can also run the implementation file directly:

```sh
uv run python src/calculator_project/calculator.py
```

Expected output:

```text
OK: divide(1, 0) raised ZeroDivisionError as expected
All tests passed!
```

## How the code works

In `def add(a: float, b: float) -> float`, `a` and `b` are parameters, `float`
describes the intended numeric inputs, and `-> float` describes the return value.
The docstring explains the function's contract. `return a + b` sends the result
back without changing any shared state. Python also accepts integer inputs for
these numeric operations; type hints describe intent and do not enforce types
at runtime. Callers should supply ordinary finite numbers, not strings.

`assert add(2, 3) == 5` calls the function and checks its result. A wrong result
raises `AssertionError`. Run normally, without Python's `-O` option, because
optimization disables assertions. `try` and `except` check the expected error
from division by zero.

The `if __name__ == "__main__"` guard runs the tests when the file is executed
directly, while allowing the functions to be imported without running them.

## Boundary laboratory

| Case | Input | Expected behavior |
| --- | --- | --- |
| Normal | `divide(12, 4)` | Return `3.0` |
| Boundary | `multiply(5, 0)` | Return `0` |
| Boundary | `divide(0, 5)` | Return `0` |
| Negative | `add(-2, 2)` | Return `0` |
| Invalid | `divide(1, 0)` | Raise `ZeroDivisionError` |
| Stretch | `percentage_change(100, 120)` | Return `20` |
| Boundary | `compound_growth(1000, 0.05, 0)` | Return `1000` |
| Invalid | `percentage_change(0, 120)` | Raise `ValueError` |
| Invalid | `compound_growth(1000, 0.05, -1)` | Raise `ValueError` |

The code includes eleven assertions plus three explicit expected-error checks.
Each error check raises `AssertionError` if the expected exception is missing,
so a failed check cannot silently continue to the success message.

For compound growth, supply a whole number of periods and a decimal rate
(`0.05` means 5%). The `int` hint does not reject fractional periods at runtime.
Percentage change uses the signed old value as its denominator; a zero old
value is rejected. These functions assume ordinary finite numeric inputs.

## Debugging the class example

`divide(12 / 4)` supplies just one argument, so Python raises `TypeError` because
`b` is missing. The corrected call is `divide(12, 4)`. An assertion placed after
`return` inside the same function is unreachable; checks belong outside that
function. The corrected check `assert divide(12, 4) == 3` passes.

## Business/design interpretation

The outputs can support simple decisions such as calculating a total or an
average cost per item. The main assumption is that the inputs are meaningful
numbers expressed in compatible units. Division by zero is rejected because
it cannot produce a valid ratio. Floating-point rounding remains a limitation,
so this beginner example is not an exact accounting calculator.

## Exit ticket — personalize before submitting

- One concept I can now explain: ____________________
- One boundary I tested: ____________________
- One question I still have: ____________________
- One line of code I would improve: ____________________
