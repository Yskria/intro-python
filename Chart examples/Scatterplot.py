import pandas as pd
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]  # x-axis values
y = [2, 4, 6, 8, 10]  # y-axis values

# Create a scatter plot
plt.scatter(x, y)

# Customize the plot
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()