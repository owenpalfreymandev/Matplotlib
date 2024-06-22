import numpy as np
import matplotlib.pyplot as plt

bands = ["C++", "C#", "Python", "Java", "Ruby"]
monthly_listeners = [20, 29, 163, 12, 44]

plt.bar(bands, monthly_listeners, align="edge", width=0.5, edgecolor="orange", lw=6)
plt.show()