def in_asc_order(arr):
    return arr == sorted(arr)

'''
Description:

Are the numbers in order?

In this Kata, your function receives an array of positive integers as input. Your task is to determine whether
the numbers are in ascending order.

For the purposes of this Kata, you may assume that all inputs are valid (i.e. arrays containing only positive
integers with a length of at least 2).

For example:

in_asc_order([1,2,4,7,19]) # returns True
in_asc_order([1,2,3,4,5]); // returns True
in_asc_order([1,6,10,18,2,4,20]) # returns False
in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order
Extra Challenge: If time, try to optimise and shorten your code as much as possible.
'''
