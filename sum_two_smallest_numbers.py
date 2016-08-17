def sum_two_smallest_numbers(numbers):
    x = sorted(numbers)
    return x[0] + x[1]

print sum_two_smallest_numbers([10,2,3,4,5,6])


"""
refactored:


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

"""