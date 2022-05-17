from math import pi
# 2) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

# 2) Has a function to calculate the circumference of a circle
def area(length, width):
    return length * width

def circumference(radius):
    return round(2 * pi * radius, 1)

