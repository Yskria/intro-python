import matplotlib.pyplot as plt
import numpy as np

def f(s):
    return 5*s + 0.2*s**3

x_values = np.linspace(0, 10, 500)    # Generate values of x (500 values of x between 0 and 10)
y_values = f(x_values)    

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='5*s + 0.2*s**3')   # Giving a label that appears in the legend (if printed)
plt.title('Example of a plot')                      # Title of the plot
plt.xlabel("x")                                     # Name of the x-axis
plt.ylabel("y")                                     # Name of the y-axis
plt.xlim([0,10])                                     # Range of x-axis
plt.ylim([0,250])                                    # Range of y-axis
plt.grid(True)                                      # Plotting gridlines
plt.legend(loc='upper left')                        # Plot the legend in the upper left corner
plt.show()


print (7**5)