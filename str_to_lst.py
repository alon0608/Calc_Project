from xmlrpc.client import boolean



from Custom_Exception_Class import *
from Minus_Check import minus_checker
from Operators_dict import Operators
from exception_checker import exceptions_checker


def splitter(expression):
    """
    Splits the input mathematical expression into individual elements (numbers, operators, etc.).
    - Handles decimal numbers and ensures valid decimal placement.
    - Removes unnecessary spaces and tabs.
    - Calls minus_checker to process unary minus.
    - Calls exceptions_checker to validate the final list of elements.

    Args:
        expression (str): The mathematical expression to split.

    Returns:
        list: A list of elements (numbers, operators, etc.) after processing.

    Raises:
        InvalidDecimalPlacementError: If a decimal is placed incorrectly.
        ConsecutiveDecimalsError: If there are multiple consecutive decimals.
    """
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