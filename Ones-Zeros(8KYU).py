def binary_array_to_number(arr):
    strarr = [str(i) for i in arr]
    binary =  ''.join(strarr)
    return int(binary, 2)


print(binary_array_to_number([1,0,1,1,1]))