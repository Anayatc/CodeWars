def accum(s):
    a = []
    for i, letter in enumerate(s, 1):
        a.append(i * letter)
    x = "-".join(a)
    return x.title()




x = 'abccba'

print accum(x)

'''
This time no story, no theory. The examples below show you how to write function accum:
'''