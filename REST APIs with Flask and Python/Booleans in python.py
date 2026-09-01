# -- Comparisons --

print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. not recommended to use it 

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False