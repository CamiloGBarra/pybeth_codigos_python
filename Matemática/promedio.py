import numpy as np

print(np.average([1, 2, 3]))

# generalización
def promedio(*args):
    return np.average(args)

print(promedio(1, 2, 3))
print(promedio(1, 2, 3, 4, 5))
print(promedio(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))