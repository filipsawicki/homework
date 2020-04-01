def validBraces(string):
    temp = []
    for item in string:
        if item in ['[','{','(']:
            temp.insert(0, item)
