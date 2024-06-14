import sys
"""
    importing argv from sys
"""


argv = sys.argv


NESTED_MORSE = {' ': '/ ',
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
                '0': '-----'}


def valid_char():
    if len(argv) < 2:
        raise AssertionError("the arguments are bad")
    else:
        for x in argv[1]:
            if not x.isdigit() and not x.isalpha() and x != " ":
                raise AssertionError("the arguments are bad")


def main():
    valid_char()
    decoded = [NESTED_MORSE[x.upper()]
               for x in argv[1] if x.islower() or x == " " or x.isdigit()]
    for x in decoded:
        print(x, end=" ")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
