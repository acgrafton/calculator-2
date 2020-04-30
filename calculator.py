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
        y = float(command_list[2])

        if operator == "+":
            print(add(x,y))

        elif operator == "-":
            print(subtract(x,y))




run_prefix_calculator()
