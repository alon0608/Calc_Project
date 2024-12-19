class CalculatorError(Exception):
    """Base class for calculator exceptions."""
    def __init__(self, message="An error occurred in the calculator"):
        super().__init__(message)

class CalculatorInputError(CalculatorError):
    """Raised for invalid input."""
    def __init__(self, message=None):
        super().__init__(message or "Input cannot be empty. Please enter an expression.")

class DivisionByZeroError(CalculatorError):
    """Raised for division by zero."""
    def __init__(self, message=None):
        super().__init__(message or "You cannot divide by zero.")

class ParenthesisMismatchError(CalculatorError):
    """Raised for mismatched parentheses."""
    def __init__(self, message=None):
        super().__init__(message or "Mismatched parentheses detected.")

class IllegalCharacterError(CalculatorError):
    """Raised for illegal characters."""
    def __init__(self, character):
        super().__init__(f"Illegal character detected: '{character}' is not allowed.")

class ZeroPowerByZero(CalculatorError):
    """Raised for 0^0."""
    def __init__(self, message=None):
        super().__init__(message or "You cannot compute zero raised to the power of zero.")

class OverFlowResult(CalculatorError):
    """Raised for overflow in result."""
    def __init__(self, message=None):
        super().__init__(message or "Result exceeds the maximum allowable.")

class OverFlowResultPow(CalculatorError):
    """Raised for overflow in pow expression."""
    def __init__(self, message=None):
        super().__init__(message or "Result exceeds the maximum allowable for pow.")

class OverFlowResultFactorial(CalculatorError):
    """Raised for overflow in factorial."""
    def __init__(self, message=None):
        super().__init__(message or "Result exceeds the maximum allowable for factorial.")

class MinOverFlowResult(CalculatorError):
    """Raised for result below minimum."""
    def __init__(self, message=None):
        super().__init__(message or "Result exceeds the minimum allowable.")

class TooMuchOperatorsInARow(CalculatorError):
    """Raised for consecutive operators."""
    def __init__(self, op1, op2):
        super().__init__(f"Cannot place '{op1}' after '{op2}'.")

class TwoOrMoreTildas(CalculatorError):
    """Raised for multiple tildas."""
    def __init__(self):
        super().__init__("Cannot place more than one tilde before a number.")

class MissingOperandError(CalculatorError):
    """Raised for missing operand."""
    def __init__(self, operator, message=None):
        super().__init__(message or f"Missing operand after operator '{operator}'.")

class EmptyParentheses(CalculatorError):
    """Raised for empty parentheses."""
    def __init__(self):
        super().__init__("Expression is missing inside parentheses.")

class NegativeFactorial(CalculatorError):
    """Raised for negative factorial."""
    def __init__(self):
        super().__init__("Cannot compute factorial of a negative number.")

class NegativeFactorialSum(CalculatorError):
    """Raised for negative factorial sum."""
    def __init__(self):
        super().__init__("Cannot compute factorial sum of a negative number.")

class FloatFactorialSum(CalculatorError):
    """Raised for float factorial sum."""
    def __init__(self):
        super().__init__("Cannot compute factorial sum of a float number.")

class FloatFactorial(CalculatorError):
    """Raised for float factorial."""
    def __init__(self):
        super().__init__("Cannot compute factorial of a float number.")

class ConsecutiveDecimalsError(CalculatorError):
    """Raised for multiple decimals in a number."""
    def __init__(self):
        super().__init__("Multiple consecutive decimal points detected.")

class LeadingOperatorError(CalculatorError):
    """Raised for leading operator without operand."""
    def __init__(self, op):
        super().__init__(f"Expression cannot start with '{op}' without a preceding operand.")

class InvalidDecimalPlacementError(CalculatorError):
    """Raised for invalid decimal placement."""
    def __init__(self):
        super().__init__("Invalid placement of decimal point.")

class NegativeSqrt(CalculatorError):
    """Raised for square root of a negative number."""
    def __init__(self):
        super().__init__("Cannot compute square root of a negative number.")

class MissingOperatorAfterFactorials(CalculatorError):
    """Raised for missing operator after factorial."""
    def __init__(self, char):
        super().__init__(f"Cannot place a number right after '{char}'.")

class MissingOperator(CalculatorError):
    """Raised for missing operator between tokens."""
    def __init__(self, char, op):
        super().__init__(f"Missing operator between '{char}' and '{op}'.")
