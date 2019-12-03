# Exercise 4: To play with variables.
cars = 100 # Number of cars available
space_in_a_car = 4.0 # Space available in each car
drivers = 30 # Number of drivers present 
passengers = 90 # Numnber of passangers present
cars_not_driven = cars - drivers # Number of cars that will not be in any use today
car_driven = drivers # Number of cars driven today
carpool_capacity = car_driven * space_in_a_car # Total capacity of carpool available for today
average_passengers_per_car =  passengers / car_driven # average passengers per car


print("There are ", cars , " cars available.") # Printing the number of car available
print("There are only ", drivers," drivers are availabe.") # Printing the number of drivers present
print("There will be ", cars_not_driven, "empty cars today.") # Printing the empty cars today
print("We can transport ", carpool_capacity, " people today.") # Printing the number of people we can transport today
print("We have ", passengers, " to carpool today.") # Printing total passengers available for car pool
print("We need to put about ", average_passengers_per_car, " in each car.") # Printing the average passenger needs to be put in each car
