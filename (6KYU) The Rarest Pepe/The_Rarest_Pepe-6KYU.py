def find_rarest_pepe(pepes):
    from collections import Counter
    counts = Counter(pepes)
    least_pepes = min(counts.values())
    low_pepes = [i for i, j in counts.items() if j == least_pepes]
    return 'No rare pepes!' if least_pepes >= 5 else low_pepes.pop() if len(low_pepes) == 1 else sorted(low_pepes)

pepe_sample = ['Codewars Pepe',
               'Codewars Pepe',
               'Codewars Pepe',
               'Codewars Pepe',
               'Codewars Pepe']

pepe_sample2 = ['Deep Learning Pepe',
               'Go Pepe',
               'Machine Learning Pepe',
               'Machine Learning Pepe',
               'Machine Learning Pepe']

pepe_sample3 = ['Donald Trump Pepe',
               'Melania Trump Pepe',
               'Clown Pepe',
               'Clown Pepe',
               'Donald Trump Pepe']

print(find_rarest_pepe(pepe_sample))
print(find_rarest_pepe(pepe_sample2))
print(find_rarest_pepe(pepe_sample3))