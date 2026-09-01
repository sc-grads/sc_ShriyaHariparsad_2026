name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"

print(greeting)

greeting = f"Hello, {name}"
print(greeting)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)