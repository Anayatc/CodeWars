def broken(inp):
    return ''.join(['0' if i == '1' else '1' for i in inp])

print(broken('1101001011110'))

'''
Description:

The bloody photocopier is broken... Just as you were sneaking around the office to print off your favourite binary code!

Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string.
'''