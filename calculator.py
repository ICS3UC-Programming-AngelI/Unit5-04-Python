# !/usr/bin/env python3
# Created by: Angel
# Created on May 12,2025
# This programs the user for two numbers and the
# sign of code they want.


def find_result(num_1, num_2, operator_str):
    if operator_str == "%":
        return num_1 % num_2
    if operator_str == "*":
        return num_1 * num_2
    if operator_str == "/":
        return num_1 / num_2
    if operator_str == "+":
        return num_1 + num_2
    if operator_str == "-":
        return num_1 - num_2


def main():
    user_num_1 = 0
    user_num_2 = 0
    operator_str = 0
    try:
        user_num_1 = float(input("Enter the first number: "))
        user_num_2 = float(input("Enter the second number: "))
        operator_str = input("Enter an operator (+,-,%,*,/): ")
        print("")

        if user_num_1 <= 0 and user_num_2 <= 0:
            print("This is not a good number")
        else:
            if (
                operator_str == "%"
                or operator_str == "*"
                or operator_str == "+"
                or operator_str == "%"
                or operator_str == "-"
            ):
                result = find_result(user_num_1, user_num_2, operator_str)
            print(result)
    except:
        print("Please enter a valid value.")


if __name__ == "__main__":
    main()
