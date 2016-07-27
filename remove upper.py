def lowercase_count(strng):
    new =
    for i in strng:
        if i.islower():
            i += str(new)
    return new

print lowercase_count('aaaAbfB')