
yourname = input('Hi, Whats your name? ')
yourage = input('Well, Hello ' + str(yourname) + ' how old are you? ')

def hundred(yourage):
    if yourage.isdigit() == True:
        x = (2016 - int(yourage)) + 100
        print('you will be one hundred years old in the year ' + str(x))
    else:
        return 'Error your age must be a number!'


print(hundred(yourage))

