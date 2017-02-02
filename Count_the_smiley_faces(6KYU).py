from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

'''
#before refactoring
def count_smileys(arr):
    count = 0
    acceptedSmiley = [';)',':)',':D',';D',';-)',':-)',':-D',';-D',';~)',':~)',':~D',';~D',]
    for i in arr:
        if i in acceptedSmiley:
            count +=1
    return count
'''
print(count_smileys([':)',':(',':D',':O',':;']))