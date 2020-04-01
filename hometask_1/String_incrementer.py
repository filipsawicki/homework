"""
Write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

    foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

"""


def increment_string(data) -> str:
    temp_str = ""
    temp_int = []


    for i in range(len(data)):
        char = data[i]
        if char.isalpha():
            temp_str += "" + char

        else:
            char.isdigit()
            temp_int.append(int(char))

    temp_int[-1] += 1

    result = temp_str + "".join([str(i) for i in temp_int])
    return result







print(increment_string("foobar1"))

print(increment_string("foobar23"))


