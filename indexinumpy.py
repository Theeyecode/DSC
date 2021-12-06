import numpy as np
# creating a sample array
# arr = np.arange(0, 11)
# print('The sample array is:', arr)
# arr[:5] = 100
# print('The sample array is:', arr)

# indxing a 2D array(matrices)

arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
print(arr_2d)
print(arr_2d[1])
print(arr_2d[1, 0])
print(arr_2d[:2, 1:])
print(arr_2d[2, :])

arr = np.arange(10, 51)
print(arr)
