def divisible_by_ref(list,number):
    return [x for x in list if x % number == 0]

print(divisible_by_ref([1,2,3,4,5,6],2))


'''
def divisible_by(list,number):
    x = []
    for item in list:
        if item % number == 0:
            x.append(item)
    return x
'''

'''
Description:

Write a function which takes two arguments and returns all number, which are divisible by given divisor. First argument is array of numbers and the second is divisor.

Example

divisible_by([1,2,3,4,5,6], 2) == [2,4,6]
'''