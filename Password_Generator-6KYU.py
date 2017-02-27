import random

def password_gen():
    chars, digits = list('abcdefghijklmnopqrstuvwxyz'), list('1234567890')
    length = random.randint(6,20)
    passwrd = [random.choice(chars).upper() for i in range(random.randint(1, length -2))]
    passwrd += [random.choice(chars) for i in range(random.randint(1, length-len(passwrd)-1))]
    passwrd += [random.choice(digits) for i in range (length - len(passwrd))]
    random.shuffle(passwrd)
    return ''.join(passwrd)

print(password_gen())

'''
Description:

You need to write a password generator that meets the following criteria:

6 - 20 characters long
contains at least one lowercase letter
contains at least one uppercase letter
contains at least one number
contains only alphanumeric characters (no special characters)
Return the random password as a string.

Note: No character should occur more than once in an average of 100 tests.

'''