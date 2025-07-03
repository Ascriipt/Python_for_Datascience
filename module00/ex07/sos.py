import sys


NESTED_MORSE = {
    ' ': '/ ',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}


def valid_char(argv: list):
    """
    Checks if the command line arguments are valid.
    Ensures exactly one argument is provided (besides the script name) and that all characters
    in the argument are translatable into Morse code (alphanumeric or space).
    
    Args:
        argv (list): List of command line arguments.
    
    Raises:
        AssertionError: If the number of arguments is incorrect or if any character is invalid.
    """
    if not len(argv) == 2:
        raise AssertionError("the arguments are bad")
    
    for x in argv[1]:
        if x.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")


def main():
    """
    Main function to convert a given string to Morse code.
    Validates the input, converts each character to Morse code using NESTED_MORSE,
    and prints the result.
    
    Raises:
        AssertionError: If the input is invalid.
    """
    try:
        argv = sys.argv
        valid_char(argv)
        decoded = [NESTED_MORSE[x.upper()] for x in argv[1]]
        print(*decoded)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
