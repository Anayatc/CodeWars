def list_animals(animals):
    return ''.join('{}. {}\n'.format(i,j) for (i,j) in enumerate(animals, 1))


print(list_animals([ 'dog', 'cat', 'elephant', 'lion' ]))


