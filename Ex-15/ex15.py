# Ecercise 15: How to read a file.

from sys import argv # Importing the module

script, filename = argv # Passing the variable during run time

txt = open(filename) # Opening the file mentioned for filename

print(f"Here's your file {filename}:") # Printing the file name
print(txt.read()) # Reading the contents from the opened file

print("Type the file name again:") # Print statement
file_again = input("> ") # Taking input

txt_again = open(file_again) # Opening the file mentioned in file_again

print(txt_again.read()) # Reading the file
#print(txt.read()) # Remember to close to file as the cursor will reach to the EOF
#print("Strange")
