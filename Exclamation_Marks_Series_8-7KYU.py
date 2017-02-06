def remove(s):
    return s.replace('!','')+ s.count('!')* '!'

print(remove("Hi! Hi!! Hi!"))

'''
Description:

Move all exclamation marks to the end of the sentence
Examples

remove("Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!!"
remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"
Note

Please don't post issue about difficulty or duplicate.
'''