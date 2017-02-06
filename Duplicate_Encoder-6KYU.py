def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

'''
before refactoring:

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
'''

print duplicate_encode('dIn din')

'''
Description:

The goal of this exercise is to convert a string to a new string where each character in the new string
is '(' if that character appears only once in the original string, or ')' if that character appears more
than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("
'''