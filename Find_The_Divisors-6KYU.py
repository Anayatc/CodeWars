from functools import reduce


def divisors(n):
    x = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    if len(x) >= 3:
        return sorted(x[2:])
    else:
        return '%d is prime' % n


print(divisors(15))

'''
Description:

Create a function named divisors that takes an integer and returns an array with all of the integer's divisors(except
for 1 and the number itself). If the number is prime return the string '(integer) is prime' (use Either String a
in Haskell).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
You can assume that you will only get positive integers as inputs.
'''