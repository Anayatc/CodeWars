elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']


def chinese_zodiac(year):
    return elements[(year%10)//2-2]+" "+animals[year%12-4]

print (chinese_zodiac('1990'))
