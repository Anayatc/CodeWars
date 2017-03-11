import functools
import operator

def persistence(n):
    count = 0
    while n > 9:
<<<<<<< HEAD
        n = (functools.reduce(operator.mul, [int(i) for i in str(n)], 1))
        count += 1
=======
        y = (functools.reduce(operator.mul, [int(i) for i in str(n)], 1))
        n = y
        count +=1
>>>>>>> 13cd5609d1e1341e7f77dd916a314bd3d50e65da
    return count



<<<<<<< HEAD
print(persistence(999))
=======
print(persistence(39))
>>>>>>> 13cd5609d1e1341e7f77dd916a314bd3d50e65da

'''
Description:

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
'''