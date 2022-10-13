"""This module is for classification of traingle"""


# method for classification
def classify_triangle(side_a, side_b, side_c):
    if side_a > 200 or side_b > 200 or side_c > 200:
        return 'InvalidInput'

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'

    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'

    if (side_a >= (side_b + side_c)) or (side_b >= (side_a + side_c)) or (side_c >= (side_a + side_b)):
        return 'NotATriangle'

    if side_a == side_b and side_b == side_a and side_c == side_b:
        return 'Equilateral'
    elif ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2):
        return 'Right'
    elif ((side_b ** 2) + (side_c ** 2)) == (side_a ** 2):
        return 'Right'
    elif ((side_a ** 2) + (side_c ** 2)) == (side_b ** 2):
        return 'Right'
    elif (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    else:
        return 'Isoceles'
