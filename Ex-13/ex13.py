# Exercise 13: Program to import any module and using the function from it

from sys import argv # Importing the modules 

# read the WYSS section for how to run this

script, first, second, third = argv # Assignment of arguments using argv to unpack the values

#Printing the variables
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)