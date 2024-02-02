#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    for i in range(int(x)):
        try:
            print("{}".format(my_list[i]), end="")
            elements += 1
        except IndexError:
            pass
    print()
    return elements
