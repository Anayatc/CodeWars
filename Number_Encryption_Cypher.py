d = {
    'I':'1', 'R':'2', 'E':'3', 'A':'4', 'S':'5', 'G':'6', 'T':'7', 'B':'8', 'O':'0',
    'l':'1', 'z':'2', 'e':'3', 'a':'4', 's':'5', 'b':'6', 't':'7', 'g':'9', 'o':'0',
}

def cypher(string):
    result = string
    for i in string:
        if i in d:
            result = result.replace(i,d[i])
    return result



print cypher('hello world IREASGTBOlizeasbtgo')