def remove_smallest(numbers):
    numbers.remove(min(numbers))
    return numbers

print remove_smallest([1,2,3,4])