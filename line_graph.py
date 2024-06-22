import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)] # Creates 16 years
weights = [80, 83, 84, 85, 86, 82, 79, 80, 
           80, 83, 78, 85, 84, 84, 79, 80]

plt.plot(years, weights)
plt.show()