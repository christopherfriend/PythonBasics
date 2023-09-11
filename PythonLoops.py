# While Loops:

counter = 0

while counter < 3:
    print("something")
    counter += 1

# While Loop Challenge:
userNum = int(input("Please enter a number"))
sumNumbers = 0

while userNum > 0:
    sumNumbers += userNum
    userNum -= 1

print(str(sumNumbers))

# For Loops:
word = "house"

for letter in word:
    print(letter)

# For Loop Challenge:
charString = str(input("Please enter a word or phrase"))
charCounter = 0

for letter in charString:
    charCounter += 1

print(str(charCounter))

# Range:
one_input = range(5)
two_inputs = range(5, 10)
three_inputs = range(1, 20, 3)  # Increments three integers one through 19.

for num in one_input:  # Returns integers zero through four.
    print(num)

for num in two_inputs:
    print(num)  # Returns integers five through nine.

for num in three_inputs:  # Returns 1, 4, 7, 10, 13, 16, 19
    print(num)

