from cs50 import get_string, get_int
import re

options = [1, 2, 3, 4, 5, 6, 7, 8]

i = None

while i not in options:
    i = get_int("Height: ")

spaces = i - 1

for a in range(i):
    hashes = a + 1

    for b in range(spaces):
        print(" ", end="")
    for c in range(hashes):
        print("#", end="")
    print("  ", end="")
    for c in range(hashes):
        print("#", end="")
    print()

    spaces -= 1
