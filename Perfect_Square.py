import math

def find_next_square(sq):
    a = math.sqrt(sq)
    if a%1 == 0:
        return (a+1)**2
    else:
        return -1

print find_next_square(123)








