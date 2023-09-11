# Miles per Gallon Challenge
import random

gallonsGas = random.randint(10, 25)
refuelDistance = random.randint(200, 400)


def calculateMPG(maxGals, maxMiles):
    return int(maxMiles // maxGals)


print(str(gallonsGas) + " gallons and " + str(refuelDistance) + " max miles means the vehicle gets " + str(calculateMPG(gallonsGas, refuelDistance)) + " MPG.")

