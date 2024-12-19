from Operators_dict import Operators
from math_operations import Calculator
from Custom_Exception_Class import LeadingOperatorError, OverFlowResult,MinOverFlowResult


def post_calc(expression):
    """Calculate the postfix expression and returns the result"""
    result=[]
    while len(expression)!=0:
        factorial_minus_check = False
        sqrt_minus_check=False
        char=expression[0]
        if char in ("!","#"):
            """if char in !,# check if result>0 if not raise LeadingOperatorError
                else calculate the number"""
            if len(result)==0:
                raise LeadingOperatorError(char)
            num1 = result.pop()
            if char=="!":
                result.append(str(Calculator.factorial(float(num1))))
            elif char == "#":
                result.append(Calculator.factorial_sum(num1))
            expression.pop(0)
        elif char in ("<","~","_"):
            """calculate the negation of the number"""
            num1 = result.pop()
            result.append(str(Calculator.negation(float(num1))))
            expression.pop(0)
        elif char in Operators:
            """the rest of the operators, check if there are at least two numbers in result
                if not raise LeadingOperatorError else calculate the expression"""
            if len(result)<=1:
                raise LeadingOperatorError(char)
            num2=result.pop()
            num1=result.pop()
            if char=="+":
                result.append(str(Calculator.add(float(num1), float(num2))))
            elif char=="-":
                result.append (str(Calculator.subtract(float(num1), float(num2))))
            elif char=="*":
                result.append(str(Calculator.mul(float(num1), float(num2))))
            elif char=="/":
                result.append(str(Calculator.div(float(num1), float(num2))))
            elif char=="%":
                result.append(str(Calculator.modulus(float(num1), float(num2))))
            elif char=="^":
                result.append(str(Calculator.pow1(float(num1), float(num2))))
            elif char=="@":
                result.append(str(Calculator.average(float(num1), float(num2))))
            elif char=="$":
                result.append(str(Calculator.max(float(num1), float(num2))))
            elif char=="&":
                result.append(str(Calculator.min(float(num1), float(num2))))
            expression.pop(0)
        else:
            result.append(expression.pop(0))

    if result[0] == 'inf':
        raise OverFlowResult
    elif result[0] == '-inf':
        raise MinOverFlowResult
    else:
        return float(result[0])