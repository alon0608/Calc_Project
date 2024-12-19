from itertools import filterfalse
from symbol import continue_stmt

from lib2to3.fixer_util import String
from os import remove
from Custom_Exception_Class import TwoOrMoreTildas, MissingOperandError,NegativeFactorial,NegativeFactorialSum,NegativeSqrt,TooMuchOperatorsInARow
import Operators_dict
from Operators_dict import Operators

def minus_checker(lst):
    """
    param expression:
        lst (list): A list of tokens representing the parsed input expression.

    Returns:
        list: Updated list with right minuses and tilde operators properly processed.
"""
    count=0
    index=0
    tilda_check=0
    while index<len(lst) :
        is_unary_before = False
        if is_unary(lst,index,tilda_check) :
            while index<len(lst) and lst[index]=="-":
                lst[index]="<"
                is_unary_before=True
                index+=1
        elif lst[index]=="~":
            count+=1
            tilda_exception(lst,index,count,tilda_check)
            tilda_check=1
        elif lst[index] in Operators and count==0 and index!=0 and lst[index-1]!="(" and lst[index] not in ("!","#") :
            count+=1
        elif lst[index]=="-":
            lst[index]="_"
            count+=1
        else:
            count=0
        if is_unary_before==True:
            index-=1
        index+=1
    return lst

def is_unary(lst,index,tilda_check):
    """
    param expression:
        lst (list): A list of tokens representing the parsed input expression.
        index (int): The current index in the list being evaluated.
        tilda_check (int): A flag indicating whether a tilde operator has been encountered previously.

    Returns:
        bool: True if the minus sign is unary, False otherwise.
    """
    return (index == 0 and lst[index] == "-" and tilda_check == 0) or (
            index != 0 and lst[index - 1] == "(" and lst[index] == "-" )

def tilda_exception(lst,index,count,tilda_check):
    if index==len(lst)-1:
        raise MissingOperandError("~")
    elif  index!=0 and lst[index-1] in ("<","_") :
        raise TooMuchOperatorsInARow("~","-")
    elif tilda_check==1 and lst[index-1]!="(":
        raise TwoOrMoreTildas()
