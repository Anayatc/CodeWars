def f(n):
    if instance(n, int):
        list = range(1,int(n+1),1)
        return sum(list)
    else:
        return 'error'



def f1(n):
    sum = 0
    for i in range(n):
        sum += i
        return sum

print f(100)