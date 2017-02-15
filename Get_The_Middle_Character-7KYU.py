def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]

'''
def get_middle(s):
    if len(s) % 2 == 0:
        index = (len(s) - 1)/2
        return s[index] + s[index + 1]
    else :
        index = (len(s) - 1) / 2
        return s[index]

'''

print get_middle('Anyat')


'''
Description:

You are going to be given a word. Your job is to return the middle character of the word. If the word's length
is odd, return the middle character. If the word's length is even, return the middle 2 characters.

Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
Input

A word (string) of length 0 < str < 1000

Output

The middle character(s) of the word represented as a string.
'''