# Functions

# Here are some imports:
import random
print(random.randint(1, 10))

# Basic Function:
def printFour():
    print("four")


printFour()


# Functions with Parameters
def mathFunc(x, y):
    answer = int(x) + int(y)
    print(answer)


mathFunc(4, 6)

# Finding the volume of a rectangular prism:
length = int(input("Please enter the length:"))
width = int(input("Please enter the width:"))
height = int(input("Please enter the height"))


def findVolumePrism(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(findVolumePrism(length, width, height)) + " cubic feet")
