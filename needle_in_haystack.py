def find_needle(haystack):
    haystack = str(haystack)
    if not haystack:
        return "None"
    elif any("needle" in x for x in haystack):
        return "found the needle at position " + str(haystack.index("needle"))


test = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print find_needle(test)