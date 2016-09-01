def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        numbers.remove(min(numbers))
        return numbers

print remove_smallest([])