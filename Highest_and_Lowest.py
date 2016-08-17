def high_and_low(numbers):
    results = map(int, numbers.split())
    numbers = "%s %s" %(max(results), min(results))
    return numbers


print high_and_low('5,3,2,1')