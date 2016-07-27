def add_binary(a, b):
    data = a + b
    return bin(data)

def add_binary_one(a,b):
    return bin(a+b)[2:]

print add_binary(6, 6)
print add_binary_one(6, 6)
