import numpy as np
from numpy.random import randn

# my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(np.array(my_matrix))
# print(np.eye(4))

# print(np.random.randint(1, 5,))
# ranarr = np.random.randint(1, 50, 10)
# print(ranarr)
# print('The maximum number is:', ranarr.max(),
#       'Its index is :', ranarr.argmax())
# print('The minimum number is:', ranarr.min(),
#       'Its index is :', ranarr.argmin())

# arr = np.arange(25)
# print(arr)
# print(arr.reshape(5, 5))
# x = np.random.randint(0, 25, 25)

# print(x.reshape(5, 5))

np.random.seed(101)
randomNumber = randn(5, 3)

print(randomNumber)
