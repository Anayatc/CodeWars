def make_password(phrase):
    output = ''
    chars = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5',}
    for i in phrase.split():
        output += i[0]
    for key, value in chars.items():
        output = output.replace(key, value)
    return output



print(make_password("should work for some examples"))

'''
Description:

One suggestion to build a satisfactory password is to start with a memorable phrase or sentence and make a password by extracting some letters from it.

Even better is to replace some of those letters with numbers (e.g., the letter “O” can be replaced with the number “0”).

• instead of including “i” or “I” put the number “1” in the password;

• instead of including “o” or “O” put the number “0” in the password;

• instead of including “s” or “S” put the number “5” in the password.

Examples: makePassword "Give me liberty or give me death" -> "Gml0gmd" makePassword "Keep Calm and Carry On " -> "KCaC0"
'''