import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 1000
y_data = np.random.random(50) * 1000

plt.scatter(x_data, y_data, c="#00f", s=150, marker="*", alpha=0.3)
plt.show()