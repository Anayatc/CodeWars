# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    if a and b and c < 90:
        return 1
    elif a or b or c == 90:
        return 2
    elif a or b or c > 90:
        return 3
    elif a + b + c != 180:
        return 0
    elif a or b or c == 180:
        return 0

print triangle_type(180,0,0)
