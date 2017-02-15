def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

'''
import re
def disemvowel(string):
    result = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
    return result
'''

print disemvowel('hfvlyhiffvjufvhnyfuedzrrsdwewqwes')

'''
Description:

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
'''