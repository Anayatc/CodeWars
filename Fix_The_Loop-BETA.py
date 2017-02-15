def list_animals(animals):
    return ''.join('{}. {}\n'.format(i,j) for (i,j) in enumerate(animals, 1))


print(list_animals([ 'dog', 'cat', 'elephant', 'lion' ]))


'''
Description:

Your collegue write an simple loop to list his favourite animals. But there seems to be a minor mistake. Fix it!:)

If You put list of Your favourite animals to the function, You should get list of the animals with ordering and newlines. For example:

animals = [ 'dog', 'cat', 'elephant' ]

Should return:

'1. dog\n2. cat\n3. elephant\n'
'''