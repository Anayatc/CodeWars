def double_every_other(lst):
    lst[1::2] = [x * 2 for x in lst[1::2]]
    return lst

print double_every_other([1,2,3,4,5,6])

"""
Write a function, doubleEveryOther, that doubles every second integer in a list starting from the left.

In Python: The input list must not be modified.
"""