# !/usr/bin/env python3
# -*- coding: utf-8 -*-


class Calculator:

    def __init__(self,
                 first_number,
                 second_nubmer,
                 action):
        self.first_number = first_number
        self.second_nubmer = second_nubmer
        self.action = action
        self.do_action()

    def addition(self):
        return (self.first_number + self.second_nubmer)

    def difference(self):
        return (self.first_number - self.second_nubmer)

    def division(self):
        return (self.first_number / self.second_nubmer)

    def multiplication(self):
        return (self.first_number * self.second_nubmer)

    def exponentiation(self):
        return (self.first_number ** self.second_nubmer)

    def do_action(self):
        if self.action == "+":
            print(self.addition())
        elif self.action == "-":
            print(self.difference())
        elif self.action == "/":
            print(self.division())
        elif self.action == "*":
            print(self.multiplication())
        elif self.action == "**":
            print(self.exponentiation())
        else:
            print("Unknown action")



if __name__ == "__main__":
    # both input number are presumably integer
    first_number = int(input())
    action = str(input())
    second_number = int(input())
    Calculator(first_number=first_number,
               second_nubmer=second_number,
               action=action)
