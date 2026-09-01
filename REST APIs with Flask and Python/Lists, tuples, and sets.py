l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

s.add("Shriya")
print(s)

# Access individual items in lists and tuples using the index.

print(l[0])
print(t[0])
# print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.

l[0] = "Shriya"
# t[0] = "Shriya"  # This gives an error because tuples are "immutable".

print(l)
print(t)

# Add to a list by using `.append`

l.append("Jen")
print(l)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`

s.add("Jen")
print(s)

# Sets cannot have the same element twice.

s.add("Bob")
print(s)