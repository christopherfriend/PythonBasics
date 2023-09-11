aString = "This is a string."

# Printing parts of a string:
print(aString[:3])  # First point to third point.
print(aString[2:5])  # Second point to fifth point.
print(aString[4:])  # Fourth pointy to last point.

# Concatenation
r2 = "R2"
d2 = "D2"
newString = r2 + " - " + d2
print(newString)
print(newString[5:] + newString[2:5] + newString[:2])  # Flipping things around!

# Other
exampleVar = True
print(type(exampleVar))  # Print the type of variable.
exampleVar = str(exampleVar)  # Change the variable type to a string.
print(type(exampleVar))
# /t is used for tab spaces and /n is used for new lines in strings.
# \" ... \" is used to add quotes in a string. These are all called "Escape Sequences".

# Input Function
name = input("Please enter your name.")
print("Your name is " + name + ".")

inputExample = input("Please enter your favorite number.")
inputExample = int(inputExample)
inputExample += 5
inputExample = str(inputExample)
typeExample = str(type(inputExample))
print("Your favorite number plus five is " + inputExample + " and the variable type is " + typeExample + ".")

