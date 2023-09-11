# FizzBuzz

counter = 0

while counter <= 50:
    if (counter % 3 == 0) and (counter % 5 == 0):
        print("FizzBuzz")
        counter += 1
    elif (counter % 3 == 0) and (counter % 5 != 0):
        print("Buzz")
        counter += 1
    elif (counter % 3 != 0) and (counter % 5 == 0):
        print("Fizz")
        counter += 1
    else:
        print(str(counter))
        counter += 1