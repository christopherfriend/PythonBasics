def factorial(fac_num):
    returned = 1
    for num in range(fac_num, 1, -1):  # Starting at a given integer and iterating downwards by one.
        returned *= num
    return returned


print(factorial(3))


