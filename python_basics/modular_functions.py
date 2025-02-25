import math
def calculate_area(shape, dimension1, dimension2 = 0):
    if shape == "circle":
        return math.pi * dimension1**2
    if shape == "rectangle":
        return dimension1 * dimension2
    if shape == "triangle":
        return 0.5 * dimension1 * dimension2


print(calculate_area("circle", 7))
print(calculate_area("rectangle", 11, 18))
print(calculate_area("triangle", 10, 20))