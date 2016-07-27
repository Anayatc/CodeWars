import string
import collections

def encryptor(key, message):
    key = key * -1
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    upper.rotate(key)
    lower.rotate(key)
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    return message.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))

print encryptor(25, '')