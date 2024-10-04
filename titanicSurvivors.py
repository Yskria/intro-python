import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/titanic.csv')
labels = ['male', 'female', 'age']
pd.set_option('display.max_columns', None)
print(df.head())


grouped_data = df[(df['Survived'] < 1) & (df['Sex'] == 'male') & (df['Age'] < 18 )].value_counts()
#groupedDataAmountOfFemales = df[df['Sex'] == 'female'].value_counts()
#groupedDataAmountOfMales = df[df['Sex'] == 'male'].value_counts()
print(grouped_data)
#print(groupedDataAmountOfFemales)
#print(groupedDataAmountOfMales)

#plt.bar(grouped_data.index, grouped_data.values, color='blue')
#plt.show()

#The graph of choice to view all information