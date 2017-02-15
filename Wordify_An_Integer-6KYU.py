
d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
     19: 'nineteen', 20: 'twenty',
     30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
     70: 'seventy', 80: 'eighty', 90: 'ninety'}

def wordify(n):
    k = 1000
    m = k * 1000
    if n < 20:
        return d[n]
    if n < 100:
        if n % 10 == 0: return d[n]
        else: return d[n // 10 * 10] + ' ' + d[n % 10]
    if n < k:
        if n % 100 == 0: return d[n // 10] + ' hundred'
        else: return d[n // 100] + ' hundred ' + wordify(n % 100)
    if n < m:
        if n % k == 0: return wordify(n // k) + ' thousand'
        else: return wordify(n // k) + ' thousand, ' + wordify(n % k)


print(wordify(9490))

'''
Description:

Turn a given number (an integer > 0, < 1000) into the equivalent English words. For the purposes of this kata, no hyphen is needed in numbers 21-99.

Examples:

wordify(1) == "one"
wordify(12) == "twelve"
wordify(17) == "seventeen"
wordify(56) == "fifty six"
wordify(90) == "ninety"
wordify(326) == "three hundred twenty six"
Based on "Speech module" mission from Checkio.
'''
