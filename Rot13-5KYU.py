import string
import collections

def rot13(message):
    key = 13
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    upper.rotate(key)
    lower.rotate(key)
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    return message.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))

print(rot13('Anayat'))

'''
Description:

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english
alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
'''