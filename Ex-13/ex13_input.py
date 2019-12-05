# Exercise 13_input: To take input from user to use sys module

from sys import argv

print("Enter any value:")
a=input() 
script, b = argv

print("The script is: ", script)
print("The second variable is: ", b)
print("The value entered is: ", a)
