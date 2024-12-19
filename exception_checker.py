from Custom_Exception_Class import *
from Operators_dict import Operators
def exceptions_checker(final_list):
    """
    Args:
    final_list (list): A list of tokens representing the parsed input expression.

     Raises:
        CalculatorInputError: If the token list is empty.
        DivisionByZeroError: If division by zero occurs.
        IllegalCharacterError: If an unrecognized or invalid character is found.
        ParenthesisMismatchError: If parentheses are mismatched.
        EmptyParentheses: If parentheses do not enclose valid content.
        TooMuchOperatorsInARow: If multiple operators appear in sequence without valid operands.
        MissingOperatorAfterFactorials: If no operator is present after a factorial symbol.
        MissingOperator: If an operator is missing between numbers or parentheses.
        MissingOperandError: If an operator lacks a corresponding operand.

    Returns:
        None:if the list Passes all tests its continue to the next func else raises error
"""
    if not final_list:
        raise CalculatorInputError("Input list cannot be empty.")

    left_parenthesis = 0
    is_num_between = False
    consecutive_operators = 0
    first_operator = ""
    prev_char = ""

    for i, char in enumerate(final_list):
        # Check for division by zero
        if char == "/" and i + 1 < len(final_list) and final_list[i + 1] == "0":
            raise DivisionByZeroError("Division by zero is not allowed.")

        # Check for illegal characters
        if (
                not char.isdigit()  # Not a digit
                and char not in ("~","!","@","#","$","%","^","&","*","(",")","+","-","/")  # Not a valid operator
                and not char.lstrip("-").rstrip("!").isdigit()  # Not a valid number
                and not "." in char  # Not a decimal point
        ):
            raise IllegalCharacterError(char)

        # Check for balanced parentheses
        if char == "(":
            left_parenthesis += 1
            is_num_between = False
        elif char == ")":
            left_parenthesis -= 1
            if left_parenthesis < 0:
                raise ParenthesisMismatchError("Closing parenthesis without matching opening parenthesis.")
            if not is_num_between:
                raise EmptyParentheses()
        else:
            is_num_between = True

        # Check for consecutive operators
        if char in Operators and char not in("~","-"):
            consecutive_operators += 1
            if consecutive_operators == 1:
                first_operator = char
            elif consecutive_operators > 1 and (prev_char not in("!","#") ):
                raise TooMuchOperatorsInARow(char, first_operator)
        elif prev_char in ("!", "#") and char!=")" and not char in Operators:
            raise MissingOperatorAfterFactorials(prev_char)
        elif char=="(" and prev_char not in Operators and i!=0:
            raise MissingOperator(prev_char,char)
        elif prev_char in("!","#") and char=="~":
            raise TooMuchOperatorsInARow(char, prev_char)
        elif prev_char==")" and char not in Operators and char not in("(",")") :
            raise MissingOperator(char,prev_char)
        else:
            consecutive_operators = 0

        # Update previous character for further checks
        prev_char = char

    # Final checks after the loop
    if left_parenthesis > 0:
        raise ParenthesisMismatchError("Unclosed opening parenthesis detected.")

    if consecutive_operators == 1 and prev_char not in ("!","#") or prev_char in ("~","-"):
        raise MissingOperandError(prev_char)

