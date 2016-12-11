import re

def decipher_this(string):
    return ' '.join(map(lambda a, b: a+b, [chr(int(i)) for i in re.findall(r'\d+', string)], [i[-1] + i[1:-1] + i[0] if len(i)>= 2 else i for i in re.sub(r'\d+', '', string).split(' ')]))


# before refactoring

def decipherThis(string):
    words_list = re.sub(r'\d+', '', string).split(' ')
    swapped_letters = [i[-1] + i[1:-1] + i[0] if len(i)>= 2 else i for i in words_list]
    ascii_letter = [chr(int(i)) for i in re.findall(r'\d+', string)]
    return ' '.join(map(lambda a, b: a+b, ascii_letter, swapped_letters))


print(decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka'))


'''
Description:


Decipher this!
You are given several secret messages you need to decipher. Here are the conditions:

The first letter corresponds to ASCII character code (case sensitive)
The second letter needs to be switched to the last letter
The last letter needs to be switched to the second letter
If it only has one letter, it will be unchanged
If it only has two letters, you will just need to convert the ASCII character code to a letter
Keepin' it simple -- there are no special characters

Example:
decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'

'''