from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	if len(family) < 1 :
		raise ValueError("Family appears very empty :'(.");
	for i in family :
		if len(i) != len(family[0]) :
			raise TypeError("One or multiple values are of different sizes.")
	print(f"The shape of image is: ({len(family)}, {len(family[0])})");
	return family[start:end];

img = np.asarray(Image.open('./module01/animal.jpeg'))
# for i in img:
# 	print(img[i])
print(slice_me(img[0]))