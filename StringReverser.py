# String Reverser

userString = input("Please enter a string to be reversed.")


def string_reverser(string):
    new_string = ""

    for s in string:
        new_string = s + new_string

    print(new_string)


string_reverser(userString)


