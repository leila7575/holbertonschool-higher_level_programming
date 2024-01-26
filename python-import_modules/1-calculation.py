#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5
    addition = calculator.add(a, b)
    substraction = calculator.sub(a, b)
    multiplication = calculator.mul(a, b)
    division = calculator.div(a, b)
    print(f"{a} + {b} = {addition}")
    print(f"{a} - {b} = {substraction}")
    print(f"{a} * {b} = {multiplication}")
    print(f"{a} / {b} = {division}")
