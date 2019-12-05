# Exercise 20: Combining files and functions

from sys import argv # Importing the modules

script, input_file = argv # Unpacking the argv

# Fucntion to print the complete file.
def print_all(f):
    print(f.read())

# Function to set cursor back to initial position.
def rewind(f):
    f.seek(0)

# Function to print a particular lines from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Opening the inputed file.

current_file = open(input_file)

print("First let's print the whole file:\n")

# Function calling

print_all(current_file)

print("\nNow let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines:\n")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
