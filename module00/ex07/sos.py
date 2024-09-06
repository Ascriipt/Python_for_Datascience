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


def valid_char(argv : list):
    if not len(argv) == 2:
        raise AssertionError("the arguments are bad")
    else:
        for x in argv[1]:
            if not x.isdigit() and not x.isalpha() and x != " ":
                raise AssertionError("the arguments are bad")


def main():
    try:
        argv = sys.argv
        valid_char(argv)
        decoded = [NESTED_MORSE[x.upper()]
                   for x in argv[1] if x.islower() or
                   x.isupper() or x == " " or x.isdigit()]
        print(*decoded)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
