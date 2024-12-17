from Custom_Exception_Class import *
from Operators_dict import Operators
def exceptions_checker(final_list):

    if not final_list:
        raise CalculatorInputError("Input list cannot be empty.")


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

