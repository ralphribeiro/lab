# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import math

v = np.array([4, 1])
w = 5 * v
w1 = 0.1 * w
w2 = 0.2 * w
w3 = 0.3 * w
w4 = 0.4 * w
print(w, w1, w2, w3, w4)

print("w = ", w)

# Plot w
origin = [0], [0]
plt.grid()
plt.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))
plt.quiver(*origin, *w, scale=10)
plt.quiver(*origin, *w1, scale=10)
plt.quiver(*origin, *w2, scale=10)
plt.quiver(*origin, *w4, scale=10)
plt.show()
