import numpy as np
import matplotlib.pyplot as plt
import math
def f(x):
    return x
x = np.linspace ( start = 0.    # lower limit
                , stop = 4    # upper limit
                , num = 500      # generate 51 points between 0 and 3
                )
y = f(x)    # This is already vectorized, that is, y will be a vector!
plt.plot(x, y)
plt.show()