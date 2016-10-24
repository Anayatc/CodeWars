
import random
x = open('/Users/Anayat/CloudStation/PycharmProjects/CodeWars/sowpods.txt')
lines = x.read().splitlines()
myline = random.choice(lines)
print(myline)
x.close()


'''
This program returns a random word from a scrabble standard dictionary txt file
'''
