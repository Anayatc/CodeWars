def find_average(nums):
    return sum(nums) / float(len(nums)) if nums else 0

print find_average([5, 7, 3, 7])