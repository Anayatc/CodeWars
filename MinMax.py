def min(arr):
    arr.sort()
    return arr[0]

def max(arr):
    arr.sort(reverse=True)
    return arr[0]


print max([1,2,3,4,5,-1])


