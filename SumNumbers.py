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



print get_sum(-1,-10)
