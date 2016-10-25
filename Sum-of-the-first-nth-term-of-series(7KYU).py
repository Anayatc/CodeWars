def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


'''
before refactoring

def series_sum(n):
    if n == 0:
        return ("%.2f" % 0)
    else:
        n = n-1
        sum_list = [1]
        while n > 0:
            x = 1/float(n *3 +1)
            sum_list.append(x)
            n = n - 1
        return ("%.2f" % sum(sum_list))



# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + 1/19 + 1/22 +
        # 0    1     2      3       4      5    6       7
'''
print series_sum(9490)


"""
Task:

Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:

You need to round the answer upto 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.
Examples:

SeriesSum(1) => 1 = "1"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

"""