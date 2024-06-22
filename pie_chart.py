import numpy as np
import matplotlib.pyplot as plt

languages = ["C++", "C#", "Python", "Java", "Ruby"]
votes = [20, 29, 98, 12, 44]

plt.pie(votes, labels=languages) # The pie chart will be based on the number of 'votes', and the tags will be 'languages'
plt.show()