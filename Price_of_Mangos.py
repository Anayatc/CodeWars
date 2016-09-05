def mango(quantity, price):
    if quantity % 3 == 0:
        return ((quantity/3)*2)*price
    else :
        remainder = quantity % 3
        return (((quantity/3)*2) + remainder) * price


print mango(4,1)