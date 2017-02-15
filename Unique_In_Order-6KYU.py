import itertools

def unique_in_order(iterable):
    return [item for item, group in itertools.groupby(iterable)]


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('AA'))
'''
Description:
Python3
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
elements with the same value next to each other and preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''