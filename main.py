# Write a function that calculates the area of a circle.
import math

def area_circle(radius):
    return math.pi * radius ** 2 

# manual testing
print(area_circle(4)) # should print ~50.27
print(area_circle(22)) # should print ~1520.53
print(area_circle(12.3)) # should print ~475.29
