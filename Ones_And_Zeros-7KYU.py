def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)

'''
def binary_array_to_number(arr):
    strarr = [str(i) for i in arr]
    binary =  ''.join(strarr)
    return int(binary, 2)
'''

print(binary_array_to_number([1,0,1,1,1]))

'''
Description:

Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
'''