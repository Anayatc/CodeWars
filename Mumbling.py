def accum(s):
    a = []
    for i, letter in enumerate(s, 1):
        a.append(i * letter)
    x = "-".join(a)
    return x.title()




x = 'abccba'

print accum(x)

aa = 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnn-Uuuuuuuuuuu'
bb = 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu'