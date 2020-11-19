from cs50 import get_string, get_int, get_float
import re
import math

# set change to negative value to invoke repeating prompt.
change = -1

# sanitize input for only positive integers.
while change < 0:
    change = get_float("Change owed: ")

# converting input to integer cents to work with.
cents = round(change * 100)

# check if the total is greater than 25 cents.

if cents >= 25:
    quarters = math.floor((cents / 25))
    cents = cents - (quarters * 25)

    dimes = math.floor((cents / 10))
    cents = cents - (dimes * 10)

    nickels = math.floor((cents / 5))
    cents = cents - (nickels * 5)

    pennies = math.floor((cents / 1))
    cents = cents - (pennies * 1)

    coins = (quarters + dimes + nickels + pennies)
    print(coins)

# check if the total is greater than 10 cents

elif cents >= 10:
    dimes = math.floor((cents / 10))
    cents = cents - (dimes * 10)

    nickels = math.floor((cents / 5))
    cents = cents - (nickels * 5)

    pennies = math.floor((cents / 11))
    cents = cents - (pennies * 1)

    coins = (dimes + nickels + pennies)
    print(coins)

# check if the total is greater than 5 cents

elif cents >= 5:
    nickels = math.floor((cents / 5))
    cents = cents - (nickels * 5)

    pennies = math.floor((cents / 1))
    cents = cents - (pennies * 1)

    coins = math.floor((nickels + pennies))
    print(coins)

# check if the total is greater than 1 cent

elif cents >= 1:
    pennies = math.floor((cents / 1))
    cents = cents - (pennies * 1)

    coins = (pennies)
    print(coins)
