import pandas as pd


#two seperate ways of reading a Dictionairy
#y = {"name" : "John", "age" : 36}
y = dict(name="John", age=36)
print(y)

#count the amount of times a letter or phrase is in a String through an f-String
str_x = "Emma. Emma."
x = str_x.count("Emma")
s = "test"
#print(f"Emma appeared {'test 'if x == 2 else 'slecht'} times")
emmaAppearance = "Emma appeared {times} times {test}"
#print(emmaAppearance.format(s, x))
print(emmaAppearance.format(times = x, test = s))

thislist = ["apple", "banana", "cherry"]
for i in range(2):
  print(thislist[i])

#Iterating through a Tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
for x in myit:
	print(x)

def f(x):
    return 2*x+1

x_values  = [0, 1, 2, 3]

#For-loops in Python
for x in x_values:
    y = f(x)
    print(y)