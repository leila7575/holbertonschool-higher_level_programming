#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5
    addition = calculator.add(a, b)
    substraction = calculator.sub(a, b)
    multiplication = calculator.mul(a, b)
    division = calculator.div(a, b)
    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, substraction))
    print("{} * {} = {}".format(a, b, multiplication))
    print("{} / {} = {}".format(a, b, division))
