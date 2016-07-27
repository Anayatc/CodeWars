import re
from collections import defaultdict

cons = 'qwrtypsdfghjklzxcvbnm'
CONS = cons.upper()

ERR = defaultdict(str)
ERR.update({x:'err' for x in cons})
ERR.update({x:'ERR' for x in CONS})

def err_bob(string):
    pieces = re.findall(r'(\w+|\W+)', string)
    return ''.join(word + ERR[word[-1]]  for word in pieces)