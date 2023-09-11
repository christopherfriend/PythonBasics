# Flow Control
vegetable = input("Please type the name of a vegetable.")

if vegetable == "corn":
    print("Yay! You said \"corn\".")
else:
    print("The vegetable is not corn.")

# Nested if/else statements:
if vegetable != "corn":
    print("Not only is the vegetable not corn, it is...")
    if vegetable == "potato":
        print("It is a healthy potato!")
    else:
        print("NOT a healthy potato")

# elif statements:
if vegetable == "tomato":
    print("You chose a tomato!")
elif vegetable == "strawberry":
    print("You choose a berry, silly!")
else:
    print("You did not choose corn, potato, tomato, or even a berry.")
