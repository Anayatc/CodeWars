import string

def find_missing_letter(chars):
    upperorlower = [letter for letter in chars if letter.islower()]
    if not upperorlower:
        for i in string.ascii_uppercase:
            if i not in chars: return i
    else:
        for i in string.ascii_lowercase:
            if i not in chars: return i


print(find_missing_letter(['A','B','D']))

