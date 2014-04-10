import math

def polygon_area(number_of_sides, length):
    area = (number_of_sides * .25) * (length ** 2) / math.tan(math.pi / number_of_sides)
    return area

print polygon_area(7, 3)
