import pandas as pd
import matplotlib.pyplot as plt

# Import data from the .csv file
df = pd.read_csv('mtcars.csv')

# Preview the first 5 rows to see how the data is imported
print(df.head())

# We will group the data by amount of cylinders, 
# and count how many cars are in the dataset for each category

grouped_data = df['cyl'].value_counts()

# Create the bar plot
# grouped_data.index creates each category, the grouped_data.values provides the counts
# in other words: the index is the x-axis, the values the y-axis
plt.bar(grouped_data.index, grouped_data.values, color='blue')

# Customize the plot
plt.title('Number of Vehicles by Cylinder')
plt.xlabel('Cylinders')
plt.ylabel('Count')

# Display the plot
plt.show()

##### Scatterplot based on dataframe. 

# You would expect that more horsepower leads to a faster completion of a 1/4 mile. 
# To see if this could be true, we plot the variables qsec and hp on a scatterplot

plt.scatter(df['hp'],df['qsec'])

# Customize the plot
plt.title('Effect of Horsepower on 1/4 Completion time')
plt.xlabel('Horsepower')
plt.ylabel('1/4 mile in seconds')

plt.show()

# To add a linear regression model, use the Seaborn library

import seaborn as sns

# Create a scatter plot with regression line and confidence interval
sns.regplot(x=df['hp'], y=df['qsec'])

# Customize the plot
plt.title('Effect of Horsepower on 1/4 Completion time')
plt.xlabel('Horsepower')
plt.ylabel('1/4 mile in seconds')

plt.show()

# Include equation and r-squared in the plot. We also need the statsmodels library

import statsmodels.api as sm

# Calculate linear regression
x_with_intercept = sm.add_constant(df['hp'])
model = sm.OLS(df['qsec'], x_with_intercept)
result = model.fit()
slope = result.params[1]
intercept = result.params[0]
r_squared = result.rsquared

# Create a scatter plot with regression line and confidence interval
sns.regplot(x=df['hp'], y=df['qsec'])

# Add linear regression equation to the plot
equation = f'y = {intercept:.2f} + {slope:.2f}x'
r_squared_text = f'R-squared = {r_squared:.2f}'
plt.text(0.5, 9, equation, ha='center')
plt.text(0.5, 10, r_squared_text, ha='center')

# Customize the plot
plt.title('Effect of Horsepower on 1/4 Completion time')
plt.xlabel('Horsepower')
plt.ylabel('1/4 mile in seconds')

# Display the plot
plt.show()