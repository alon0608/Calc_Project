from math_operations import Calculator
from Operators_dict import Operators
def in_to_post(exercise):
    """
    Converts an infix expression to a postfix expression
    returns a list representing the postfix expression
    """
    operators_lst = []
    expression = []
    current = 0

    for char in exercise:
        if char.startswith("~") and char.lstrip("~").isdigit():
            expression.append(Calculator.negation(int(char.lstrip("~"))))

        elif char.isdigit():
            expression.append(char)

        elif char.replace('.', '', 1).replace('-', '', 1).isdigit():
            expression.append(char)
        else:
            if char == "(":
                operators_lst.append(char)
            elif char == ")":
                while operators_lst and operators_lst[-1] != "(":
                    expression.append(operators_lst.pop())
                if operators_lst and operators_lst[-1] == "(":
                    operators_lst.pop()
            elif len(operators_lst) == 0 or operators_lst[-1] == "(":
                operators_lst.append(char)
            else:
                while (
                    len(operators_lst) != 0
                    and operators_lst[-1] != "("
                    and Operators[char] <= Operators[operators_lst[-1]]
                ):
                    expression.append(operators_lst.pop())
                operators_lst.append(char)

    while len(operators_lst) != 0:
        expression.append(operators_lst.pop())

    return expression
