"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def run_prefix_calculator():
    while True:
        command_string = input(">\n").lower()
        # print("str", command_string)
        
        command_list = command_string.split(" ")
        # print("list", command_list)
        operator = command_list[0]

        if operator == "q":
            break
        
        x = float(command_list[1])

        if operator == "square":
            print(square(x))

        elif operator == "cube":
            print(cube(x))

        try:
            y = float(command_list[2])

        except IndexError:
            continue

        if operator == "+":
            print(add(x,y))

        elif operator == "-":
            print(subtract(x,y))

        elif operator == "*":
            print(multiply(x,y))

        elif operator == "/":
            print(divide(x,y))

        elif operator == "pow":
            print(power(x,y))

        elif operator == "mod":
            print(mod(x,y))


run_prefix_calculator()
