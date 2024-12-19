from symtable import Class


class CalculatorError(Exception):
    """Base class for calculator exceptions."""
    def __init__(self, message="An error occurred in the calculator"):
        super().__init__(message)


class CalculatorInputError(CalculatorError):
    """Exception raised for invalid input."""
    def __init__(self, message=None):
        super().__init__(message or "Input cannot be empty. Please enter an expression.")


class DivisionByZeroError(CalculatorError):
    """Exception raised for division by zero."""
    def __init__(self, message=None):
        super().__init__(message or "You cannot divide by zero.")


class ParenthesisMismatchError(CalculatorError):
    """Exception raised for mismatched parentheses."""
    def __init__(self, message=None):
        super().__init__(message or "Mismatched parentheses detected.")


class IllegalCharacterError(CalculatorError):
    """Exception raised for illegal characters in input."""
    def __init__(self, character):
        super().__init__(f"Illegal character detected: '{character}' is not allowed in the calculator.")

class ZeroPowerByZero(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self, message=None):
        super().__init__(message or "You cannot compute zero raised to the power of zero.")
class OverFlowResult(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self, message=None):
        super().__init__(message or "Result exceeds the maximum allowable float value.")
class TooMuchOperatorsInARow(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self, op1,op2):
        super().__init__(f"You Cant put '{op1}' After '{op2}'")
class TwoOrMoreTildas(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("You Cant Put more than one tilda before a number")
class MissingOperandError(CalculatorError):
    """Exception raised when an operand is missing for an operator."""
    def __init__(self, operator, message=None):
        super().__init__(message or f"Missing operand after operator '{operator}'.")
class EmptyParentheses(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("you need to put expression in the Parentheses ")
class NegativeFactorial(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("The Calculator Cant Compute Negative Factorial")
class NegativeFactorialSum(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("The Calculator Cant Compute Negative FactorialSum")
class FloatFactorialSum(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("The Calculator Cant Compute Float FactorialSum")
class FloatFactorial(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("The Calculator Cant Compute Float Factorial")
class ConsecutiveDecimalsError(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("Multiple consecutive decimal points detected")
class LeadingOperatorError(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self,op):
        super().__init__(f"Expression cannot start with the operator '{op}' without a preceding operand")
class InvalidDecimalPlacementError(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("Invalid placement of a decimal point Please revise the number format")
class NegativeSqrt(CalculatorError):
    """Exception raised when trying to compute 0^0."""
    def __init__(self):
        super().__init__("The Calculator Cant Compute Negative Sqrt")
class MissingOperatorAfterFactorials(CalculatorError):
    """Exception raised when trying to compute 0^0."""

    def __init__(self,char):
        super().__init__(f"You cant put number right after '{char}'")

class MissingOperator(CalculatorError):
    """Exception raised when trying to compute 0^0."""

    def __init__(self,char,op):
        super().__init__(f"You need to put operator between '{char}' and '{op}'")
