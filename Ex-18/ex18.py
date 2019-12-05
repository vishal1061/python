# Exercise 18: Introduction to Functions.

# This one is like your scripts with argv.

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#Ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This one takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments
def print_none():
    print("I got nothin'.")

# Calling the function:

print_two("Vishal", "Bisht")
print_two_again("Vishal", "Bisht")
print_one("One")
print_none()

