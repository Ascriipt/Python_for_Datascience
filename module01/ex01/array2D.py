def slice_me(family: list, start: int, end: int) -> list:
	if len(family) < 1 :
		raise ValueError;
	print(f"My shape is : ({len(family)}, {len(family[0])})");
	print(f"My new shape is : ({len(family[start:end])}, {len(family[start:end][0])})")
	print(family[start:end])
	return [start, end];

family = [[1.80, 78.4],
		  [2.15, 102.7],
		  [2.10, 98.5],
		  [1.88, 75.2]]

slice_me(family, 0, 2)