def triple_double(num1, num2):
    for i in num1:
        x = num1.count(i)
        if x >= 3:
            return x

print triple_double('12122234','9490')

