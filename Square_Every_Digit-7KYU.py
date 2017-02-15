def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

'''
def square_digits(num):
    list = []
    for i in str(num):
        list.append(str(int(i)**2))
    return int("".join(list))
'''

print square_digits()


'''
Description:

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
'''