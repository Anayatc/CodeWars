def to_acronym(input):
  return ''.join(word[0] for word in input.split()).upper()


print to_acronym('cascading style sheet')

'''
def to_acronym(input):
    a = input.split(' ')
    x = []
    for i in a:
        x.append(i[0])
    y = ''.join(x)
    return y.upper()


print to_acronym('hello world')
'''

'''
Description:

Write function toAcronym which takes a string and make an acronym of it.

Rule of making acronym in this kata:

split string to words by space char
take every first letter from word in given string
uppercase it
join them toghether
Eg:

Code wars -> C, w -> C W -> CW
'''