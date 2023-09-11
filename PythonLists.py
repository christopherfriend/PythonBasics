# Lists

example_list = [1, 2, 3, 4]  # Lists can have other datatypes.

print(list("blah"))  # This will print ['b', 'l', 'a', 'h'].

print(1 in example_list)  # Returns True; can use "not in", too. You can assign this boolean result to a variable.

# List Slicing and Indexing:
# Lists start at 0.

example_list2 = [[1, 2, 3], [4, 4, 6], [7, 8, 9]]
print(example_list2[2][0])  # Returns "7". You can use this to return specific characters in a list, too.

print(example_list[-1])  # Returns "4". Negative integers start at the end of the list.

print(example_list[:2])  # Prints "[1, 2]". prints one less than the index number.

example_list[0] = 300
example_list[1:4] = [4, 89, 54]  # Changes up to but not including index four.
print(example_list)

# del and other list statements:
example_list3 = ["sun", "venus", "mars", "Earth"]
del example_list3[1]  # Removes a specific index item.
example_list3.remove("mars")  # This will only remove the first instance of "mars". Benefit: searches the entire list.
example_list3.append("uranus")
example_list3.insert(3, "jupiter")
example_list3.sort()  # Sort by least-to-greatest and alphabetical order. You can also add "reverse=True" to reverse.
example_list3.index("uranus")  # Returns the index number of "uranus" (and only the first instance of it).
best_planet = example_list3.pop(2)  # Returns the item at the second index spot.
print(best_planet)

# Note: strings are immutable, lists are mutable.
# Note: A variable containing a list is not a list; it points (references) to a list.

