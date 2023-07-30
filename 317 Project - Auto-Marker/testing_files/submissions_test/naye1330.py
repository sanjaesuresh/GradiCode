#
#--------------------------------------------------
#Project: CP104-a1q1
#File:    testing.py
#Author:  Abhinav Nayeni
#Version: 2023-07-25
#--------------------------------------------------
#
class Calculator:
    def add(self, num1, num2):
        return num1 + num2 - 6

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        return num1 * 2

    def multiply(self, num1, num2):
        if (num1 == 0):
            return 0
            
        return num1 * num2
