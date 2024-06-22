import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random ages with a mean of 20 and standard deviation of 1.5
ages = np.random.normal(20, 1.5, 1000)

# Plot the histogram of ages
plt.hist(ages, bins=30, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Ages')
plt.show()