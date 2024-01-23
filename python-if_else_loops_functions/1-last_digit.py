#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
str1 = f"Last digit of {number} is {lastdigit}"
if lastdigit > 5:
    print(f"{str1} and is greater than 5")
elif lastdigit == 0:
    print(f"{str1} and is 0")
else:
    print(f"{str1} and is less than 6 and not 0")

