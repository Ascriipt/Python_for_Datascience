from load_image import ft_load
from load_image import slice_me

array_3d_1 = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

array_3d_2 = [
    [[1, 2], [3, 4]],
    [[5, 6]],
    [[9, 10], [11, 12]]
]

array_3d_3 = []

array_3d_4 = [
    [[1, 2], [3, 4]]
]

array_3d_5 = [
    [[1, 2], [3, 4], [5, 6]],
    [[7, 8], [9, 10]],
    [[11, 12], [13, 14]]
]

array_3d_6 = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
]

array_3d_7 = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8, 9]],  # The second sub-array here has three elements.
    [[10, 11], [12, 13]]
]

array_3d_8 = [
    [[1], [2], [3]],
    [[4, 5], [6, 7]],
    [[8, 9, 10], [11, 12, 13]]
]

slice_me(array_3d_1)
slice_me(array_3d_2)
slice_me(array_3d_3)
slice_me(array_3d_4)
slice_me(array_3d_5)
slice_me(array_3d_6)
slice_me(array_3d_7)
slice_me(array_3d_8)

ft_load('./animal.jpeg')
ft_load('./landscape.jpg')
