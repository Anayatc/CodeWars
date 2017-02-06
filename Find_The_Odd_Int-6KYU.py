def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

'''
#before refactoring
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

print find_it([1,1,2,2,5,3,3,4,4])
'''

'''
Description:

Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''
