#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for number in my_list:
        result.append(bool(number % 2 == 0))
    return result
