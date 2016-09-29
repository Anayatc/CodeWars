def find_outlier(integers):
    x = [i%2 for i in integers]
    count_even = 0
    count_odd = 0
    for i in x:
        if i == 0:
            count_even += 1
        elif i == 1:
            count_odd += 1
    if count_even > count_odd:
        for i in integers:
            if i % 2 == 1:
                return i
    elif count_odd > count_even:
        for i in integers:
            if i % 2 == 0:
                return i


print find_outlier([2,4,6,7,8])