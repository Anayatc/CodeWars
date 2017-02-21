def invert(lst):
    return [i*-1 for i in lst]

print(invert([1,2,3,4,5]))
'''
Invert a given list of integer values.

Python/JS/PHP:

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers.

'''