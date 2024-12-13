from math import pow

class Calculator:
    @staticmethod
    def add(num1, num2):
        """Returns the sum of num1 and num2"""
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        """Returns num1 minus num2"""
        return num1 - num2

    @staticmethod
    def mul(num1, num2):
        """Returns the product of num1 and num2"""
        return num1 * num2

    @staticmethod
    def div(num1, num2):
        """Returns num1 divided by num2. Raises an error if dividing by zero"""
        if num2 == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return num1 / num2

    @staticmethod
    def modulus(num1, num2):
        """Returns the remainder of num1 divided by num2. Raises an error if dividing by zero"""
        if num2 == 0:
            raise ZeroDivisionError("You can't perform modulus by zero")
        return num1 % num2

    @staticmethod
    def max(num1, num2):
        """Returns the maximum of num1 and num2"""
        return num1 if num1 > num2 else num2

    @staticmethod
    def min(num1, num2):
        """Returns the minimum of num1 and num2"""
        return num1 if num1 < num2 else num2

    @staticmethod
    def average(num1, num2):
        """Returns the average of num1 and num2"""
        return (num1 + num2) / 2

    @staticmethod
    def negation(num1):
        """Returns the negation of num1"""
        return num1 * -1

    @staticmethod
    def pow(num1, num2):
        """Returns num1 raised to the power of num2"""
        return pow(num1, num2)

    @staticmethod
    def factorial(num1):
        """Returns the factorial of num1"""
        if num1 == 0 or num1 == 1:
            return 1
        return num1 * Calculator.factorial(num1 - 1)

    @staticmethod
    def factorial_sum(num1):
        """Returns the sum of the digits of num1"""
        if num1 == 0:
            return 0
        return int(num1 % 10) + Calculator.factorial_sum(int(num1 / 10))
