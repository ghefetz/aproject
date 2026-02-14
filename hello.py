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

    # Ask the user for their name, then print a personalized greeting.
    # `.strip()` removes any accidental leading/trailing spaces.
    # If input isn't available (e.g., non-interactive run), fall back to "".
    try:
        name = input("What's your name? ").strip()
    except EOFError:
        name = ""

    # Print a friendly greeting to standard output.
    if name:
        print(f"Hello, world! Nice to meet you, {name}!")
    else:
        print("Hello, world!")


if __name__ == "__main__":
    # The "guard" ensures `main()` runs only when executing this file:
    #   python hello.py
    # and not when importing it from another module.
    main()
