"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""

def namelist(names):
    temp = []
    for name in names:
        person_name = name['name']
        temp.append(person_name)
    if len(temp) == 1:
        temp_str = "".join(temp[0])
        return temp_str
    elif len(temp) == 2:
        temp_str = "".join(temp[0] + " & " + temp[1])
        return temp_str
    elif len(temp) == 0:
        return ''

    elif len(temp) > 2:
        x = len(temp) - 2
        z = len(temp) - 1
        begin_list = temp[:len(temp) - 2]
        str_begin_list = ", ".join([str(i) for i in begin_list])
        result = "".join(str_begin_list + ", " + temp[x] + " & " + temp[z])
        return result