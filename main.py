from math import pow
from postfix_calculator import post_calc
from infix_to_postfix import in_to_post
from math_operations import Calculator
from str_to_lst import splitter
from Operators_dict import Operators
from Custom_Exception_Class import *


def main():
    while True:
        try:
            lst = input("Enter your expression (type 'top omega' to exit): ").strip()


            if lst.lower() == "top omega":
                print("Goodbye!")
                break



            lst3 = splitter(lst)
            print(f"Split Expression: {lst3}")

            lst2 = in_to_post(lst3)
            print(f"Postfix Expression: {lst2}")

            result = post_calc(lst2)
            print(f"The result is: {result}")


        except CalculatorError as e:
            print(f"Calculator Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
