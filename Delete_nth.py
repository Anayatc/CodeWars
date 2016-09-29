def delete_nth(order,max_e):
    for i in order:
        if order.count(i) >= max_e:
            return i

print delete_nth([1,2,3,4,5,5,5],3)