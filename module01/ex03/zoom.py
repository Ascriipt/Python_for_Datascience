import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load

def	zoom():
	try:
		img = ft_load("./animal.jpeg")
		img = img[100:500, 450:850, :-2]
		plt.imshow(img)
		plt.show()
	except Exception as e:
		print(f"Error: {e}")
	
if __name__ == "__main__":
	zoom()