def namelist(names):
    name_list = [d['name'] for d in names]
    return name_list

print namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])