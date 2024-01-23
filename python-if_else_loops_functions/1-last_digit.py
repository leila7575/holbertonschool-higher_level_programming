#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
if number < 0:
    lastdigit *= -1

str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"

if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} {str1}")
elif lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} {str2}")
else:
    print(f"Last digit of {number} is {lastdigit} {str3}")
