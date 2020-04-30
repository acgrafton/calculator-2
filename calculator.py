"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce

def run_prefix_calculator():

    while True:
        input_string = input(">\n").lower()
        
        tokens = input_string.split(" ")
        operator, *nums = tokens

        try:
            for i, num in enumerate(nums):
                num = float(num)
                nums.pop(i)
                nums.insert(i,num)

        except ValueError:
            print("Invalid entry.")
            continue

        result = None

        if operator.lower() == "q":
            break

        elif operator == "+":
            result = reduce(add,nums)

        elif operator == "-":
            result = reduce(subtract,nums)

        elif operator == "*":
            result = reduce(multiply,nums)

        elif operator == "/":
            result = reduce(divide,nums)

        elif operator == "square":
            result = reduce(square,nums)

        elif operator == "cube":
            result = reduce(cube,nums)

        elif operator == "pow":
            result = reduce(power,nums)

        elif operator == "mod":
            result = reduce(mod,nums)

        print(result)


run_prefix_calculator()
