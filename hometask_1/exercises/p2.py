"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
 Hint: how does an even / odd number react differently when divided by 2?
"""

number = int(input(f"Chose number from 1 to 100:  "))

def even_or_odd(number):
    if number % 2 != 0:
        print(f"your number {number} is Odd")
    else:
        print(f"Your number {number} is Even!!")

even_or_odd(number)

