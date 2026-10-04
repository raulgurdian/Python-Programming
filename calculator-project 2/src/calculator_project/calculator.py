"""A typed multifunction calculator.

Session 01 — Professional Python Foundations and Functional Programming.

Run from the project folder with:
    uv run python src/calculator_project/calculator.py
"""


# --- Core operations ---

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a times b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# --- Stretch operations ---

def percentage_change(old: float, new: float) -> float:
    """Return the percentage change from old to new (100 -> 120 is 20.0).

    Edge-case policy: raises ValueError if old is 0, because we can't divide by 0.
    """
    if old == 0:
        raise ValueError("Old value cannot be 0.")
    return (new - old) / old * 100


def compound_growth(principal: float, rate: float, periods: int) -> float:
    """Return principal after growing at rate (0.05 = 5%) for some periods.

    Edge-case policy: raises ValueError if periods is negative.
    Callers should supply a whole number of periods; type hints aren't enforced.
    """
    if periods < 0:
        raise ValueError("Periods cannot be negative.")
    return principal * (1 + rate) ** periods


# --- Tests ---

def run_tests() -> None:
    """Check every function with assertions and explicit expected errors."""
    # Normal cases
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 4) == 12
    assert divide(12, 4) == 3

    # Boundary cases
    assert add(-2, 2) == 0          # a negative and a positive cancel out
    assert multiply(5, 0) == 0      # anything times zero is zero
    assert divide(0, 5) == 0        # zero divided by a number is zero

    # Catch the expected error; fail the test if no error is raised.
    try:
        divide(1, 0)
    except ZeroDivisionError:
        print("OK: divide(1, 0) raised ZeroDivisionError as expected")
    else:
        raise AssertionError("divide(1, 0) should raise ZeroDivisionError")

    # Stretch cases
    assert percentage_change(100, 120) == 20
    assert percentage_change(200, 150) == -25
    assert round(compound_growth(1000, 0.05, 2), 2) == 1102.5
    assert compound_growth(1000, 0.05, 0) == 1000   # zero periods = no growth

    try:
        percentage_change(0, 120)
    except ValueError:
        pass
    else:
        raise AssertionError("A zero starting value should raise ValueError")

    try:
        compound_growth(1000, 0.05, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative periods should raise ValueError")

    print("All tests passed!")


def main() -> None:
    """Run the calculator's tests through the project command."""
    run_tests()


if __name__ == "__main__":
    main()
