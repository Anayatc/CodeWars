from collections import Counter

def exes_ohs(xo):
    counter = Counter(xo)
    exes = counter['x'] + counter['X']
    ohs = counter['o'] + counter['O']
    if exes == ohs:
        return True
    else :
        return False

print exes_ohs('xxXo')

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


print xo('xoxoxoxoxoxo')
