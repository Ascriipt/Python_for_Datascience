import sys


def flake8():
    """
    Analyzes a given text (from command line argument or standard input) and prints:
    - Total number of characters
    - Number of uppercase letters
    - Number of lowercase letters
    - Number of punctuation marks
    - Number of spaces
    - Number of digits

    If a command line argument is provided, it analyzes that string.
    Otherwise, it prompts the user to enter text via standard input.
    Raises AssertionError if more than one argument is provided.
    """
    argv = sys.argv
    punctuation = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    if len(argv) > 2:
        raise AssertionError()
    try:
        if len(argv) > 1:
            print(f"The text contains {sum(1 for char in argv[1])} characters:")
            print(f"{sum(1 for char in argv[1] if char.isupper())} upper letters")
            print(f"{sum(1 for char in argv[1] if char.islower())} lower letters")
            print(f"{sum(1 for char in argv[1] if char in punctuation)}", end='')
            print(" punctuation marks")
            print(f"{sum(1 for char in argv[1] if char.isspace())} spaces")
            print(f"{sum(1 for char in argv[1] if char.isdigit())} digits")
        else:
            print("What is the text to count?")
            argument = sys.stdin.readline()
            print(f"The text contains {sum(1 for char in argument)} characters:")
            print(f"{sum(1 for char in argument if char.isupper())} upper letters")
            print(f"{sum(1 for char in argument if char.islower())} lower letters")
            print(f"{sum(1 for char in argument if char in punctuation)}", end='')
            print(" punctuation marks")
            print(f"{sum(1 for char in argument if char.isspace())} spaces")
            print(f"{sum(1 for char in argument if char.isdigit())} digits")
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt as e:
        print(f"Error: keyboard interupt")


def main():
    """
    Main function to execute the flake8 function and handle exceptions.
    It catches AssertionError and other exceptions, printing a specific error message.
    """
    try:
        flake8()
    except AssertionError:
        print("Error : AssertionError.")
    except Exception:
        print("Error : Exception.")


if __name__ == "__main__":
    main()
