# Celsius to Fahrenheit Challenge

celsius = int(input("Please enter a temperature in Celsius."))


def changeToFarehheit(c):
    return round((1.8 * c + 32), 1)


print("The Fahrenheit equivalent of " + str(celsius) + " Celsius is " + str(changeToFarehheit(celsius)) + " Fahrenheit.")