def duplicate_encode(word):
    wordlist = [i for i in word.lower()]
    print wordlist
    newstr = []
    for i in wordlist:
        if i == ' ':
            newstr.append(' ')
        elif wordlist.count(i) == 1:
            newstr.append('(')
        else:
            newstr.append(')')
    return ''.join(newstr)

print duplicate_encode('dIn din')