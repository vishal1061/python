# Exercise 16: Reading and Writing in the file.

from sys import argv # Importing the module

script, filename = argv # Passing the arguments during run time.

# Print statements 
print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Taking user's choice 

input("?")


print("Opening the file....")
target = open(filename, 'w') # Opening the file in write mode

print("Truncating the file, Goodbye!")
target.truncate() # Clears the contents of the file 

print("Now I'm going to ask you for three lines.")

# Taking input from user to add any new lines in the opened file. 

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these lines to the file")

# Write operation in the opened file

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we clsoe it.")

# Closing the file.

target.close()

# Output of the write operation done above.
target_again = open(filename)
print(target_again.read())
target_again.close()