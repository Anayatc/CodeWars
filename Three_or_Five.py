def solution(number):
    list_of_three = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list_of_three.append(i)
    return sum(list_of_three)

print solution(9490)