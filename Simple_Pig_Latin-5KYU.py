def pig_it(text):
    return ' '.join([i[1:]+i[0]+'ay' if i.isalpha() else i for i in list(text.split())])


print(pig_it('Pig latin is cool?'))

'''
Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'''