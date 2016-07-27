def DNA_strand(dna):
    opposite = []
    for i in dna:
        if i == 'A':
            opposite.append('T')
        elif i == 'T':
            opposite.append('A')
        elif i == 'G':
            opposite.append('C')
        elif i == 'C':
            opposite.append('G')
    return str(opposite).translate(None, ' [],\'')

print DNA_strand('ATGC')