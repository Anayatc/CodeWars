def number(lines):
    return ['{0}: {1}'.format(i +1, j) for i, j in enumerate(lines)]


print(number(["a", "b", "c"]))