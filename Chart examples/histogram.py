import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create histogram, set bar width and alignment
plt.hist(data, bins=[1, 2, 3, 4, 5, 6], width=0.5, rwidth=0.5, align='left')

# Add labels and title
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram')

# customize x-axis ticks
custom_xticks = [1, 2, 3, 4, 5]
plt.xticks(custom_xticks)

# Show plot
plt.show()