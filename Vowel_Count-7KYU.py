def getCount(inputStr):
    x = inputStr.lower()
    a = x.count('a')
    b = x.count('e')
    c = x.count('i')
    d = x.count('o')
    e = x.count('u')
    return a + b + c + d + e


print(getCount('hello world'))

'''
Description:

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.
'''