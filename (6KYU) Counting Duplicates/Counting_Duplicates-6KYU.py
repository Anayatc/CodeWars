def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

'''
def duplicate_count(text):
    dict = {i:text.count(i) for i in set(text.lower())}
    count = 0
    for i in dict.values():
        if i > 1:
            count += 1
    return count
'''

print(duplicate_count('aabbcde'))

'''
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that 
occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, 
including digits, uppercase and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
"aa11" -> 2 # 'a' and '1'
'''