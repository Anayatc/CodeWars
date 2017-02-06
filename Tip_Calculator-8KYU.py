import math

ratings = {'terrible': 1.00, 'poor': 1.05, 'good': 1.10, 'great': 1.15, 'excellent': 1.20}

def calculate_tip(amount, rating):
    for keys, values in ratings.items():
        if rating.lower() == keys:
            tip = values * amount - amount
            return int(math.ceil(tip))
    else:
        return "Rating not recognised"


print(calculate_tip(1000, 'excellent'))

'''
Description:

Write a function, calculateTip(amount, rating) which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive. If an unrecognised rating is input, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
Because you're a nice person, you always round up the tip, regardless of the service.

'''