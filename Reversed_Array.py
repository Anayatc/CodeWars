def digitize(n):
    a = str(n)[::-1]
    return [int(char) for char in str(a)]

print digitize(193)