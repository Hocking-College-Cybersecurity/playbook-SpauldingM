"""Repeatable calculator"""

from typing import Optional


def get_number(prompt: str) -> float:
    """Prompt repeatedly until the user enters a valid float; handles Ctrl+C."""
    while True:
        try:
            raw = input(prompt).strip()
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 3.14).")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            raise SystemExit(1)


def format_num(x: Optional[float]) -> str:
    """Format numbers for display; None => 'undefined'."""
    if x is None:
        return "undefined"
    return f"{x:.6g}"


def choose_operation() -> str:
    """Show menu and return the selected operation as one of '+', '-', '*', '/'."""
    menu = (
        "Please select an operation:\n"
        "1. Addition (+)\n"
        "2. Subtraction (-)\n"
        "3. Multiplication (*)\n"
        "4. Division (/)\n"
        "5. Exit\n"
        "Enter 1-5 or + - * / (5 to exit): "
    )
    while True:
        choice = input(menu).strip()
        if choice in ("1", "+"):
            return "+"
        if choice in ("2", "-"):
            return "-"
        if choice in ("3", "*", "x", "X"):
            return "*"
        if choice in ("4", "/"):
            return "/"
        if choice in ("5", "exit", "Exit", "EXIT", "q", "quit"):
            return "exit"
        print("Invalid selection. Please choose 1-5 or + - * / (5 to exit).")


def main() -> None:
    print("My Python Calculator\n")
    while True:
        try:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
        except SystemExit:
            return

        op = choose_operation()

        if op == "exit":
            print("Exiting.")
            break

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0.0:
                result = None
            else:
                result = num1 / num2
        else:
            # Shouldn't happen
            print("Unexpected operation.")
            break

        # Display
        print()
        print(f"({format_num(num1)} {op} {format_num(num2)}) = {format_num(result)}")
        print()


if __name__ == "__main__":
    main()