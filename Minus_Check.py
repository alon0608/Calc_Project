from os import remove
import Operators_dict
from Operators_dict import Operators
from os import remove
import Operators_dict
from Operators_dict import Operators


def minus_checker(lst):
    count=0
    number=1
    index=0
    tilda_check=0
    while index<len(lst) :
        if is_unary(lst,index,tilda_check) :
            lst[index]="<"
            count+=1
        elif index==len(lst)-1 and lst[index]=="~":
            raise MissingOperandError("~")
        elif lst[index]=="~" and (index!=0 and lst[index-1] in ("<","-") and count>0):
            raise TooMuchOperatorsInARow("~","-")
        elif lst[index]=="~":
            if tilda_check==1:
                raise TwoOrMoreTildas()
            tilda_check=1
            index+=1
            count+=1
        elif lst[index] in Operators and count==0 and index!=0 and lst[index-1]!="(" and lst[index] not in ("!","#") :
            count+=1
            index+=1
        elif lst[index]=="-":
            number*=-1
            count+=1
            lst.pop(index)
        elif isinstance(lst[index],int) or isinstance(lst[index],float) or lst[index].isdigit():
            lst[index] = int(lst[index])
            count=0
            lst[index]*=number
            tilda_check = 0
            number=1
            lst[index]=str(lst[index])
            index+=1
        elif lst[index]=="(" and is_minus_before_parenthesis(number,tilda_check):
            if lst[index-1]=="~":
                lst[index-1]="_"
            else:
                lst.insert(index,"_")
            index+=2
            number=1
            tilda_check=0
        elif lst[index]=="(" and not is_minus_before_parenthesis(number,tilda_check):
            if lst[index-1]=="~":
                lst.pop(index-1)
                index-=1
            number=1
            tilda_check=0
            index+=1
        else:
            index+=1
    return lst
def is_unary(lst,index,tilda_check):
    if (index == 0 and lst[index] == "-" and tilda_check == 0) or (
            index != 0 and lst[index - 1] == "(" and lst[index] == "-" and tilda_check == 0):
        return True
def is_minus_before_parenthesis(number,tilda_check):
    return (number==1and tilda_check==1) or (number==-1 and tilda_check==0)