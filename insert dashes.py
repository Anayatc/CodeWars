def insert_dash(num):
    num = str(num)
    for i in num:
        if i % 2 == 0:
            i.append('-')

print insert_dash(1224466771)