from PIL import Image
import matplotlib as plt
import numpy as np


def ft_load(path: str) -> list:
    try:
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise IOError("not in JPG or JPEG format")
        im = Image.open(path)
        print("The shape of image is: ", end="")
        print(f"({im.size[1]}, {im.size[0]}, {im.layers})")
        return np.array(im)

    except IOError as e:
        print(f"IOError: {e}")
    except Exception as e:
        print(f"RuntimeError: {e}")