def square_digits(num):
    list = []
    for i in str(num):
        list.append(str(int(i)**2))
    return int("".join(list))

print square_digits()