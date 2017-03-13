def namelist(names):
    return ' & '.join(', '.join([i['name'] for i in names]).rsplit(', ', 1))



print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'} ]))


'''
Description:

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be
separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''