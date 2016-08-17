def get_middle(s):
    if len(s) % 2 == 0:
        index = (len(s) - 1)/2
        return s[index] + s[index + 1]
    else :
        index = (len(s) - 1) / 2
        return s[index]

print get_middle('Anyat')


"""
refactored:


def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]


"""