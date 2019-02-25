import numpy as np

a = np.arange(1.0,2.0,0.1)
print(a)
print(a.any())
b = 1.5

for val in a:
    if np.isclose(b, val, atol=1.e-3):
        print('yay')

