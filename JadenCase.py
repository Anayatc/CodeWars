import string

def toJadenCase(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

print toJadenCase('hello world')