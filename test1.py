A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10) #0,1,2,3,4,5,6,7,8,9
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0]) #1,2,3,4,5
A4 = [i for i in A1 if i in A3] #12345
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

#print A6


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1]) #3,2,1,0,1,2
f(3)

'''

def e(2, l=[0,1]):
    for i in range(2): #0,1
        l.append()
'''