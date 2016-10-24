def double_every_other(lst):
    lst[1::2] = [x * 2 for x in lst[1::2]]
    return lst

print double_every_other([1,2,3,4,5,6])