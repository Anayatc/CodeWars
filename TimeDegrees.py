"""def clock_degree(s):
    hr, min = s.split(':')
    if int(hr) > 12:
        return str((int(hr)-12)*30)
    elif int(hr) == 0:
        return str((int(hr)+12)*30)
    elif int(hr) > 24:
        return "Check your time !"
    elif int(hr) < 0:
        return "Check your time !"
    else:
        return int(hr) * 30

def clock_degree_min(x):
    hour, mn = x.split(':')
    if int(mn) == 60:
        return 360
    elif int(mn) == 0:
        return 360
    elif int(mn) > 60:
        return "Check your time !"
    elif int(mn) < 0:
        return "Check your time !"
    else:
        return int(mn) * 6

"""


def clock_degree(s):
    h, m = [float(n) for n in s.split(":")]
    result = []
    for n, denominator in (h, 12), (m, 60):
        result.append((n % denominator) / denominator * 360)
    return str(int(result[0])) + ':' + str(int(result[1]))

print clock_degree("00:00")