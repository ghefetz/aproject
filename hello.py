"""A tiny "Hello, world!" script.

This module demonstrates a common Python pattern:
- put the program's work in a `main()` function
- only run it when the file is executed directly (not when imported)
"""


def main() -> None:
    """Program entry point.

    The return type annotation (`-> None`) indicates this function is used for
    its side effects (printing), not for returning a value.
    """

    # Print a friendly greeting to standard output.
    print("Hello, world!")


if __name__ == "__main__":
    # The "guard" ensures `main()` runs only when executing this file:
    #   python hello.py
    # and not when importing it from another module.
    main()
