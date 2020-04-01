def is_isogram(string):
    temp = set()
    for i in string:
        temp.add(",".join(i.lower()))
    if len(string) == len(temp) or len(string) == 0:
        return True
    return False


is_isogram("Dermatoglyphics")
is_isogram("abbddtseko")

is_isogram("moOse")