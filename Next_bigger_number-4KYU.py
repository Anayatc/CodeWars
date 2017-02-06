import itertools

def next_bigger(n):
    print()
    pos_comb = ''.join(map(str,[i for i in itertools.permutations([int(d) for d in str(n)])]))



print(next_bigger(12))