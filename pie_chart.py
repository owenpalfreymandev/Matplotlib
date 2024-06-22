import numpy as np
import matplotlib.pyplot as plt

languages = ["C++", "C#", "Python", "Java", "Ruby"]
votes = [20, 29, 98, 12, 44]
explodes = [0, 0.2, 0, 0, 0] # Brings out the second item in the array slightly
color = ["blue", "purple", "yellow", "orange", "red"] # Customizes the color of each item in the pie chart

plt.pie(votes, labels=languages, explode=explodes, colors=color, autopct="%.1f%%") # The pie chart will be based on the number of 'votes', and the tags will be 'languages'
plt.show()