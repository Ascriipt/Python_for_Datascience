import sys

argv = sys.argv[1:]

try:
    for i in argv:
        if len(argv) > 1:
            raise AssertionError("more than one argument is provided")
        int(i)
        isEO = "I'm Even." if int(i) % 2 == 0 else "I'm Odd."
        print(isEO)

except AssertionError as e:
    print(f"AssertionError: {e}")

except ValueError:
    print("AssertionError: argument is not an integer")
