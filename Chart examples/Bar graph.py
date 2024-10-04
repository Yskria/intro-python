import pandas as pd
import matplotlib.pyplot as plt

# Data for the bar graph
labels = ['A', 'B', 'C', 'D']
values = [1, 4, 2, 5]

# Create the bar graph
plt.bar(labels, values, color='red')

# Add a title and axis labels
plt.title('My Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the graph
plt.show()
