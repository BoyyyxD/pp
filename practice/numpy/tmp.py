import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# arr = np.array([1, 5, 3, -10, 12, 0, -8, 12, 100])
# arr = np.reshape(arr, (3, 3))

b = np.empty((2, 3))
c = np.empty((1, 3))




print(f"{b=} {c=}")
print(f"along 0: {np.concatenate((b,c), axis=0)=}")
print(f"along 1: {np.concatenate((b,c), axis=1)=}")
