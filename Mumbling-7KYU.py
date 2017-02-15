def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

'''
def accum(s):
    a = []
    for i, letter in enumerate(s, 1):
        a.append(i * letter)
    x = "-".join(a)
    return x.title()
'''



x = 'abccba'

print(accum(x))

'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''