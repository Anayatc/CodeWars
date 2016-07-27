def list_animals(animals):
    list = ''
    for i in animals:
        list += str(i) + 1 + '. ' + animals[i] + '\n'
    return list

print list_animals( [ 'dog', 'cat', 'elephant' ])