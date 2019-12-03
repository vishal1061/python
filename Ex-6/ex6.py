# Exercise 6: Exercise about String and text

types_of_people = 10 # Initializing a varable.
x = f"There are {types_of_people} types of people." #intialization of another variable.

binary = "binary" # Initialization of another variable.
do_not = "don't" # Initialization.
y = f"Those who know {binary} and those who {do_not}." # Initialization.

print(x) # Printing x with 'types_of_people'
print(y) # Printing y with 'binary' and 'do_not'

print(f"I said: {x}") # Another way of writing x.
print(f"I also said: '{y}'") # Another way of writing y.

hilarious = False # Assigning hilarious to boolean False

joke_evaluation = "Isn't that joke so funny?! {}" # assigning joke_evaluation with a formatter
print(joke_evaluation.format(hilarious)) # Printing joke_eavaluation with value of formatter

w = "This is a left side of...." # Assigning string variable
e = "a string with a right side." # Assigning another string variable

print(w+e) #Printing 2 strings with the concatination
