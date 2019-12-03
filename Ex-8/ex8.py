# Exercise 8: Complex formatting of any string

formatter = "{} {} {} {}" # defining a formatter variable which can take four inputs using format function.

print(formatter.format(1,2,3,4)) # First type of assignment.
print(formatter.format("one", "two", "three", "four")) # Second type of assignment.
print(formatter.format(True, False, True, False)) # Third type of assignment.
print(formatter.format(formatter, formatter, formatter, formatter)) # Fourth type of assignment.
# Fifth type of asignment.
print(formatter.format("Try your", 
"Own text here", 
"May be a poem", 
"Or a song about fear"
))
