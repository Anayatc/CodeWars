import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))

'''
before refactoring
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
'''


print DNA_strand('ATGC')


'''
Description:

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the
development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one
side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never
empty or there is no DNA at all (again, except for Haskell).

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
'''