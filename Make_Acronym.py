def to_acronym(input):
    a = input.split(' ')
    x = []
    for i in a:
        x.append(i[0])
    y = ''.join(x)
    return y.upper()


print to_acronym('hello world')



#refactored

def to_acronym1(input):
  return ''.join(word[0] for word in input.split()).upper()


print to_acronym1('cascading style sheet')