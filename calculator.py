# !/usr/bin/env python3
# -*- coding: utf-8 -*-

first_number = float(input("Input first number: "))
action = str(input("Input operator: "))
second_number = float(input("Input second number: "))
if action == "+":
    print(first_number + second_number)
    print("Done")
elif action == "-":
    print(first_number - second_number)
    print("Done")
elif action == "*":
    print(first_number * second_number)
    print("Done")
elif action == "/":
    print(first_number / second_number)
    print("Done")
elif action == "**":
    print(first_number ** second_number)
    print("Done")
else:
    print("Unknown action")
