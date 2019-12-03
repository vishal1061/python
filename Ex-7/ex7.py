# Exercise 7: More play with Strings Printing

print("Marry had a little lamb.") # Printing a string.
print("Its fleece was white as {}.".format('snow')) # Printing a string with format function.
print("And everywhere taht Mary went.")
print("."*10) # What'd that do? - It will print "." 10 times.

# Assigning single charater for different variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch end = ' ' at the end. try removing it to see what happens
# end = ' ' it's default value is /n in print function but we can assign it to a new value. Here we have it assigned with a ' '. Therefore the next line is printed on same line in the output
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ') # Printing end1 to end6 with concatination and a new variable 'end' which provides a space in the end
print(end7 + end8 + end9 + end10 + end11 + end12) # Printing end7 to end12 with concatination