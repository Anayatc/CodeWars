def digital_root(n):
    while n>10:
        n = sum([int(i) for i in str(n)])
    return n



print digital_root(9499490)