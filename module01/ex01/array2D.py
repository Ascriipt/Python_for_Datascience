def slice_me(family: list, start: int, end: int) -> list:
    if len(family) < 1:
        raise ValueError("Family appears very empty :'(.")
    for i in family:
        if len(i) != len(family[0]):
            raise TypeError("One or multiple values are of different sizes.")
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print("My new shape is : (", end="")
    print(f"{len(family[start:end])}, {len(family[start:end][0])})")
    return family[start:end]


famly = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(famly, 0, 2))
except Exception as e:
    print(e)