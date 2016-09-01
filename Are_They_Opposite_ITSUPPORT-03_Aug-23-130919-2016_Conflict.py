def is_opposite(s1, s2):
    t1 = s1.lower()
    t2 = s2.lower()
    count = range(len(s1))
    if len(s1) == 0 and len(s2) == 0:
        return False
    for i in range(len(s1)):
        if (t1[i] == t2[i]) and ((s1[i].islower() == s2[i].isupper()) or (s1[i].isupper() == s2[i].islower())):
            count[i] = True
    return all(count)





print is_opposite('','')

"""if s1.islower() == s2.isupper() or s1.isupper() == s2.islower():
    return True
"""