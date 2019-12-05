# Exercise 17: Program to copy two files.

# Importing the modules
from sys import argv 
from os.path import exists

# Assigning the arguments we need to pass during running of script
script, from_file, to_file =  argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two lines on one line, how?

# Opening and reading of a file
in_file = open(from_file)
indata = in_file.read()

#print(indata)

print(f"The input file is {len(indata)} bytes long")

#Checking the existance of the file 
print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Opening the file in write mode and then writing in the file
out_file = open(to_file, "w")
out_file.write(indata)

print("Allright, all done.")

# Closing the files

out_file.close()
in_file.close()
