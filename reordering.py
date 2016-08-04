import re
def re_ordering(text):
    return re.findall('[A-Z]{1}', text)



print re_ordering('hello World')