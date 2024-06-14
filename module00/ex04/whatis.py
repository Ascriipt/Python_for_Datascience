import sys

argv = sys.argv[1:]

for i in argv:
    isEO = "I'm Even." if int(i) % 2 == 0 else "I'm Odd."
    print(isEO)
