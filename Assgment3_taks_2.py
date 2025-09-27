import math
def circle_area(radius):
    pi = math.pi
    rad = radius * radius
    return pi * rad

def circle_circumference(radius):
    pi  = math.pi
    return  2 * pi * radius

def geometry_report(radius):
    print(f" Circle with radius: {radius}\n Area: {circle_area(radius):.2f}\n Circumference: {circle_circumference(radius):.2f}")


geometry_report(5)