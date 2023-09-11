# Word Counter Challenge

userString = input("Please enter a string. I will count the number of words in your string.")


def word_counter(string):
    spaces_and_letters = ""  # We want to count only appropriate characters, per the prompt.
    word_count = 1
    for char in string:
        if char.isalnum() or char.isspace() or char == "-" or char == "'":
            spaces_and_letters += char  # Add the character back into the original string.
    for char in spaces_and_letters:
        if char.isspace():
            word_count += 1
    return word_count


print(word_counter(userString))
