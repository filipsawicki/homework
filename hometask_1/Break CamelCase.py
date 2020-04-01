"""
Complete the solution so that the function will break up camel casing, using a space between words.
Example

solution("camelCasing")  ==  "camel Casing"
"""
import re


def solution(s):
    temp = re.split("(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", s)
    return str(" ".join(temp))


print(solution("camelCasing"))


def solution_2(s2):
    temp_string = ""
    for i in range(len(s2)):
        character = s2[i]
        if character.isupper():
            temp_string += " " + character
        else:
            temp_string += character
    return temp_string


print(solution_2("camelCasing"))
