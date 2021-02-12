"""Classes in Python Example"""

class Rectangle:
    # Attributes
    # No access level modifiers in python e.g. private
    width = 0
    height = 0

    # Constructor
    # __init__ == constructor (two underscores on each side)
    # "self" == "this", refers to current object instance. 
    #   This is not implicit in Python, must include in any method that wants to use object attributes
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Calc and return area
    # No return types in function signatures in python
    def area(self):
        return (self.height * self.width)

# ---PROGRAM CODE---
# Instantiate new class object - no "new" keyword in python
r = Rectangle(10, 35)
# Can access attributes as usual
r.height = 20

# Print area using our class function
# Python automatically puts a space before arguements in print
print("Area of Rectangle:", r.area())