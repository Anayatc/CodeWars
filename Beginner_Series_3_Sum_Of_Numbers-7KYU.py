def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))

'''
def get_sum(a,b):
    if b > a:
        c = sum(range(a,b +1))
        return c
    elif b < a:
        d = sum(range(b,a +1))
        return d
    elif a == b:
        return a


def get_sum_ref(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
'''


print get_sum(-1,-10)

'''
Description:

Given two integers, which can be positive and negative, find the sum of all the numbers between including them
too and return it. If both numbers are equal return a or b.

Note! a and b are not ordered!

Example:
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
Waiting for the Feedback! Thanks!
'''