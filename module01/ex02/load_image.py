from PIL import Image

# import matplotlib.pyplot as plt
import numpy as np


def slice_me(family: list):
    try:
        if len(family) < 1:
            raise ValueError("Family appears very empty :'(.")
        expected_length = len(family[0])
        if len(family[0][0]) == 0:
            raise ValueError("Family's subvalue is empty.")
        expected_sublength = len(family[0][0])
        for x, i in enumerate(family):
            if len(i) != expected_length:
                raise TypeError("One or multiple values are of different size")
            for j in family[x]:
                if len(j) != expected_sublength:
                    raise TypeError("Substring values are of different sizes.")
        print("The shape of image is: (", end="")
        print(f"{len(family)}, {expected_length}, {expected_sublength})")
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


def ft_load(path: str) -> list:
    img = np.asarray(Image.open(path))
    slice_me(img)
    return img
