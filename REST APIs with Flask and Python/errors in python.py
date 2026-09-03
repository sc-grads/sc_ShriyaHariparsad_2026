def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


grades = []  

try:
    average = divide(sum(grades), len(grades))
    print(average)
except ZeroDivisionError as e:
    print(e)
    # Much friendlier error message because now we're dealing with it 
    .
    print("There are no grades yet in your list.")

# -- Built-in errors --

# TypeError: something was the wrong type
# ValueError: something had the wrong value
# RuntimeError: most other things



# -- Doing something if no error is raised --

grades = [90, 100, 85]

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list.")
else:
    print(f"The average was {average}")


# -- Doing something no matter what --
# This is particularly useful when dealing with resources that you open and then must close


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --") 