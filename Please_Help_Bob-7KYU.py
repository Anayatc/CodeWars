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

print err_bob('hello world')

'''
Description

In English we often use "neutral vowel sounds" such as "umm", "err", "ahh" as fillers in conversations to help
them run smoothly.

Bob always finds himself saying "err". Infact he adds an "err" to every single word he says that ends in a
consonant! Because Bob is odd, he likes to stick to this habit even when emailing.

Task

Bob is begging you to write a function that adds "err" to the end of every word whose last letter is a
consonant (not a vowel, y counts as a consonant).

The input is a string that can contain upper and lowercase characters, some punctuation but no numbers.
The solution should be returned as a string.

NOTE: If the word ends with an uppercase consonant, the following "err" will be uppercase --> "ERR".

eg:

"Hello, I am Mr Bob" --> "Hello, I amerr Mrerr Boberr"

"THIS IS CRAZY!"  --> "THISERR ISERR CRAZYERR!"
Good luck!
'''