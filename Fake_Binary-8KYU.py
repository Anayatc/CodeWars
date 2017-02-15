def fake_bin(x):
    return "".join("0" if i in "01234" else "1" for i in x)

print fake_bin('45385593107843568')

'''
Description:

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
'''