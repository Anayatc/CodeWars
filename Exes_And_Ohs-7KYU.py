def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('xoxoxoxoxoxo'))

'''
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
'''


'''
Description:

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contains any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''