def pipe_fix(s):
    mx = max(s)
    mn = min(s)
    return range(mn, mx)[::1]

print pipe_fix([1,2,3,5,6,8,9])