import sys


def flake8():
    argv = sys.argv
    punctuation = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    if len(argv) > 2:
        raise AssertionError()
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


def main():
    try:
        flake8()
    except AssertionError:
        print("AssertionError : Y'a une erreur connard.")
    except Exception:
        print("AssertionError : Y'a une erreur connard.")


if __name__ == "__main__":
    main()
