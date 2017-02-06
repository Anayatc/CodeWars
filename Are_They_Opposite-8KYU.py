def is_opposite(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2

'''
Before Refactoring
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
'''

print(is_opposite('', ''))

'''
Description:

They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it series #1:
Are they opposite?

Task

Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.
The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string

Some examples:

isOpposite("ab","AB") should return true;
isOpposite("aB","Ab") should return true;
isOpposite("aBcd","AbCD") should return true;
isOpposite("AB","Ab") should return false;
isOpposite("","") should return false;
'''