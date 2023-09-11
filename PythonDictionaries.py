# Dictionaries

console = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
print(console["microsoft"])  # Returns "xbox"
value = console["microsoft"]
print(value)

# You may mix data types within a dictionary.
# Lists must be equivalent in order to be the same, dictionaries need not be in the same order.

print("game-cube" in console)  # Returns false; you may also use "not in".
print(console.keys())  # Returns all keys.
print(console.values())  # Returns all values.
print((console.items()))  # Returns a list of tuples.

for value in console.values():
    print(value)

for key, value in console.items():
    print(key, value)

if "apple" in console:
    print(console["apple"])
else:
    print("Apple is not in the dictionary")

# OR...

print(console.get("apple", "Apple is not in the dictionary."))