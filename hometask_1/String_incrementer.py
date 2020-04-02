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

        elif char.isdigit():
            temp_int.append(int(char))

    if len(temp_int) > 0:
        number_in_list = ["".join([str(i) for i in temp_int])]
        number_list = [int(i) for i in number_in_list]
        number_list[0] += 1
        return temp_str + "".join(str(i) for i in number_list)
    else:
        return temp_str + str(1)


print(increment_string("foobar1"))

print(increment_string("foobar99"))
