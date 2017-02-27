def countBits(n):
    return bin(n).count('1')



print(countBits(1234))
'''
Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in
the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''