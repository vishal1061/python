# Exercise 26: The Test

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')    # Original Line: print("How much do you weigh?", end=' ' . Missing a perenthesis
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

import sys

filename = sys.argv

txt = open("filename.txt")

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


print("'Let's practice everything.")  # Original Line: print('Let's practice everything.'). It should be double quotes as we are using 's in the sentence. 

# print('You\'d need to know \'bout escapes   # Original Lines: """""" quotes are missing
# with \\ that do \n newlines and \t tabs.')

print("""You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")  # print("--------------). Original Line: "" qoutes are missing
print(poem)
print("--------------") # print(--------------") Original Line: "" is missing.


five = 10 - 2 + 3 # five = 10 - 2 + 3 -  Original Line. - is extra.  
print(f"This should be five: {five}")  # print(f"This should be five: {five}" . Perenthesis was missing

# def secret_formula(started) Originally no : in function defination

def secret_formula(started):    
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars + 100  # crates = jars  100. No arithmetic sign 
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # beans, jars, = secret_formula(start_point). One variable was not defined so it is giving error while returning the values

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!") # print "Too many cats! The world is doomed!" . Perenthesis is missing

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # if people > dogs ":" is missing 
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
