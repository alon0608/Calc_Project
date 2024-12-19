from math import pow, factorial
from Custom_Exception_Class import *
from decimal import Decimal
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
        """Returns the remainder of num1 divided by num2, Raise an error if dividing by zero"""
        if num2 == 0:
            raise ZeroDivisionError("You can't perform modulus by zero")
        return num1 % num2

    @staticmethod
    def max(num1, num2):
        """Returns the maximum of num1 and num2"""
        if num1 > num2:
            return num1
        return num2

    @staticmethod
    def min(num1, num2):
        """Returns the minimum of num1 and num2"""
        if num1 < num2:
            return num1
        return num2
    @staticmethod
    def average(num1,num2):
        """Returns the average of num1 and num2"""
        return (num1+num2)/2
    @staticmethod
    def negation(num1):
        """return:negation of the number it gets"""
        return num1*(-1)
    @staticmethod
    def pow1(num1,num2):
        """return:num1 power by num2
            raises:ZeroPowerByZero,NegativeSqrt,OverFlowResult"""
        if num1==0 and num2==0:
            raise ZeroPowerByZero()
        if num1<=0 and isinstance(num2,float):
            raise NegativeSqrt()
        try:
            return pow(num1,num2)
        except:
            raise OverFlowResultPow
    @staticmethod
    def factorial(num1):
        """
        returns: factorial
        raise: NegativeFactorial for negative numbers
               OverFlowFactorial for 171 or more factorial
                FloatFactorial for float number """
        if num1<0 :
            raise NegativeFactorial()
        if num1>170:
            raise OverFlowResultFactorial
        if int(num1)!=num1:
            raise FloatFactorial()
        if num1==0 or num1==1:
            return 1
        return num1*Calculator.factorial(num1-1)
    @staticmethod
    def factorial_sum(num1):
        """
        returns factorial sum
        raise: NegativeFactorialSum for negative numbers"""
        sum=0
        num2=float(num1)
        if num2<0 :
            raise NegativeFactorialSum()
        num_str=str(num1)
        for char in num_str:
            if char.isdigit():
                sum+=int(char)
        return sum

