def sum_array(arr):
    if not arr:
        return 0
    else:
        arr.sort(key = int)
        arr = arr[1:-1]
        return sum(arr)

list1 = [1,3,999,2]
print (sum_array(list1))