import re
def disemvowel(string):
    result = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
    return result

print disemvowel('hfvlyhiffvjufvhnyfuedzrrsdwewqwes')