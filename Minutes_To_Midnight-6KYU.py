import datetime

def minutes_to_midnight(d):
    date, time = str(d).split(' ')
    h,m,s = time.split(':')
    if int(s) >=30: s=1
    else: s=0
    return str(1440 - int(h)*60 - int(m) - int(s)) + ' minutes'

print 12*60 -15

today = datetime.datetime.now()
print(minutes_to_midnight2(datetime.datetime(today.year, today.month, today.day, 23, 59, 29)))

'''
def minutes_to_midnight2(d):
    date, time = str(d).split(' ')
    h,m,s = time.split(':')
    if int(s) >=30: s=1
    else: s=0
    mRemaining = 1440 - int(h)*60 - int(m) - int(s)
    if mRemaining == 1:
        return str(mRemaining) + ' minute'
    else:
        return str(mRemaining) + ' minutes'

'''

'''
Description:

Teemo is not really excited about the new year's eve, but he has to celebrate it with his friends anyway.

He has a really big passion about programming and he want's to be productive till midnight. He want's to know how many minutes he has left to work on his new project.
He doesn't want to look on the clock all the time, so he thought about a function, which returns him the number of minutes.

Can you write him a function, so he can stay productive?

The function
minutesToMidnight(d)
will take a date object as parameter. Return the number of minutes in the following format:

"x minute(s)"

You will always get a date object with of today with a random timestamp.
You have to round the number of minutes.
Milliseconds doesn't matter!

Some examples:

10.00 am => "840 minutes"
23.59 pm => "1 minute"
'''