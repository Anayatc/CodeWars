def valid_parentheses(s):
    count = 0
    for i in s:
        if i == '(': count+=1
        if i == ')': count-=1
        if count <0: return False
    return True if count == 0 else False

'''
Write a function called validParentheses that takes a string of parentheses, and determines if the order of the
parentheses is valid. validParentheses should return true if the string is valid, and false if it's invalid.

Examples:
validParentheses( "()" ) => returns true
validParentheses( ")(()))" ) => returns false
validParentheses( "(" ) => returns false
validParentheses( "(())((()())())" ) => returns true

All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'
'''