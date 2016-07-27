def divisible_by(numbers, divisor):
    for i in numbers:
        if i % divisor == 0:
            return i

print divisible_by([1,2,3,4,5,6,7,], 2)