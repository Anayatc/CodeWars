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

print rot13('Anayat')