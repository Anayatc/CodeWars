import datetime

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



def minutes_to_midnight(d):
    date, time = str(d).split(' ')
    h,m,s = time.split(':')
    if int(s) >=30: s=1
    else: s=0
    return str(1440 - int(h)*60 - int(m) - int(s)) + ' minutes'

print 12*60 -15

today = datetime.datetime.now()
print(minutes_to_midnight2(datetime.datetime(today.year, today.month, today.day, 23, 59, 29)))