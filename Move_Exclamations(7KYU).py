def remove(s):
    return s.replace('!','')+ s.count('!')* '!'

print remove("Hi! Hi!! Hi!")