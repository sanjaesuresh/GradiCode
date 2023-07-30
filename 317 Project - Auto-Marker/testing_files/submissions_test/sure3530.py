#
#--------------------------------------------------
#Project: CP104-a1q1
#File:    testing.py
#Author:  Sanjae Suresh Kumar
#Version: 2023-07-25
#--------------------------------------------------
#
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2

    def multiply(self, num1, num2):
        return num1 * num2
