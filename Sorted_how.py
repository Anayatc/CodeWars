def is_sorted_and_how(arr):
    if sorted(arr) == arr:
        return 'yes,ascending'
    elif sorted(arr, reverse=True) == arr:
        return 'yes,descending'
    else:
        return 'no'
