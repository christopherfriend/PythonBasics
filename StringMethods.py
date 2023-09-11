# String Methods

all_low = "all lowercase letters"
print(all_low.upper())

all_upper = "ALL UPPERCASE LETTERS"
print(all_upper.lower())

# .isupper() and .islower() return the boolean expected values.
# .isalpha(), isalnum(), .isdecimal(), .isspace(), .istitle() (makes the string title case) exist, too.

print("this is a string".startswith("this"))  # Returns "True"; .endswith() exists, too.

print(", ".join(["one", "two", "three"]))
print("Eggs, Milk, Waffles, Bacon".split(", "))
