# Exercise 19: More on functions

# Defining a function:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Calling function by passing direct values

print("We can just give the fuction numbers directly:")
cheese_and_crackers(20,30)

# Calling function using variables
#  
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# Calling function using math operators.

print("We can even do math inside too:")
cheese_and_crackers(50+20, 45+65)

# Calling function using variables and math operators
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 20)
