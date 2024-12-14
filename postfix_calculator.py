from idlelib.replace import replace

from Operators_dict import Operators
from math_operations import Calculator
def post_calc(expression):
    """Calculate the postfix expression and returns the result"""
    result=[]
    while len(expression)!=0:
        factorial_minus_check = False
        sqrt_minus_check=False
        char=expression[0]
        if char == "!":
            num1=result.pop()
            result.append(Calculator.factorial(num1))
            expression.pop(0)
        elif char == "#":
            num1 = result.pop()
            result.append(Calculator.factorial_sum(num1))
            expression.pop(0)
        elif char in Operators:
            num2=result.pop()
            num1=result.pop()
            if char=="+":
                result.append(Calculator.add(num1,num2))
            elif char=="-":
                result.append (Calculator.subtract(num1, num2))
            elif char=="*":
                result.append(Calculator.mul(num1, num2))
            elif char=="/":
                result.append(Calculator.div(num1, num2))
            elif char=="%":
                result.append(Calculator.modulus(num1, num2))
            elif char=="^":
                if num1<0 and num2>0 and num2<1:
                    sqrt_minus_check=True
                    num1*=-1
                if sqrt_minus_check:
                    result.append(Calculator.pow(num1, num2)*-1)
                else:
                    result.append(Calculator.pow(num1, num2))
            elif char=="@":
                result.append(Calculator.average(num1, num2))
            elif char=="$":
                result.append(Calculator.max(num1, num2))
            elif char=="&":
                result.append(Calculator.min(num1, num2))
            expression.pop(0)
        else:
            result.append(expression.pop(0))
    return result
