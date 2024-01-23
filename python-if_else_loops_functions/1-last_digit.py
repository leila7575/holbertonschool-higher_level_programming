#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
str1 = "Last digit of"
str2 = "is"
str3 = "and is greater than 5"
str4 = "and is 0"
str5 = "and is less than 6 and not 0"
if lastdigit > 5:
    print(f"{str1} {number} {str2} {lastdigit} {str3}")
elif lastdigit == 0:
    print(f"{str1} {number} {str2} {lastdigit} {str4}")
else:
    print(f"{str1} {number} {str2} {lastdigit} {str5}")
