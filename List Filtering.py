def filter_list(l):
    try:
        f = float(l)
        return 1
    except ValueError:
        return 0


list = [1,2,'ok']

print filter_list(list)