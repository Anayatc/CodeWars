def validate(n):
    digits_list =[int(i) for i in str(n)]
    if len(digits_list) % 2 == 0:
        digits_list[::2] = [i*2 for i in digits_list[::2]]

    elif len(digits_list) % 2 == 1:
        digits_list[1::2] = [i * 2 for i in digits_list[1::2]]

    digits_list = [x-9 if x > 9 else x for x in digits_list]
    sum_digits = sum(digits_list)% 10
    if sum_digits == 0:
        return True
    else :
        return False


print validate(79927398713)
print validate(79927398710)
print validate(79927398711)
print validate(79927398712)
print validate(79927398714)
print validate(2543)
print validate(2741)
print validate(2841)

'''
this function uses the Luhn Algorithm for credit card number verification.
'''