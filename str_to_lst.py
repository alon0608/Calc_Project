from xmlrpc.client import boolean



from Custom_Exception_Class import *
from Minus_Check import minus_checker
from Operators_dict import Operators
from exception_checker import exceptions_checker


def splitter(expression):

    final_list = []
    current = ""
    decimal_point_count = 0

    for index, char in enumerate(expression):
        # Check if the character is part of a number (digit or decimal point)
        if char.isdigit() or char == ".":
            if char == ".":
                # Ensure the decimal is placed correctly
                if index == 0 or (not expression[index - 1].isdigit() and not char == "."):
                    raise InvalidDecimalPlacementError()
                decimal_point_count += 1
            if decimal_point_count > 1:
                raise ConsecutiveDecimalsError()
            current += char
        else:
            # Reset decimal counter and process the current number
            decimal_point_count = 0
            if char == " ":
                current = current  # Ignore spaces
            elif current:
                final_list.append(current)
                current = ""
            # Add non-space characters to the final list
            if char not in (" ", "\t"):
                final_list.append(char)
    # Append any remaining number
    if current:
        final_list.append(current)
    exceptions_checker(final_list)
    # Process unary minus and check for exceptions
    final_list1 = minus_checker(final_list)
    return final_list1