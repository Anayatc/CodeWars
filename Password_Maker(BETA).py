def make_password(phrase):
    output = ''
    chars = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5',}
    for i in phrase.split():
        output += i[0]
    for key, value in chars.items():
        output = output.replace(key, value)
    return output



print(make_password("should work for some examples"))