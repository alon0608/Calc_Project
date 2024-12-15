from os import remove

import Operators_dict
from Operators_dict import Operators


def minus_checker(lst):
    count=0
    number=1
    index=0
    tilda_check=0
    while index<len(lst) :
        if lst[index]=="~" and count<=1 and lst[index+1]!="~":
            tilda_check=1
            lst.pop(index)
        elif lst[index] in Operators and count==0 and index!=0:
            count+=1
            index+=1
        elif lst[index]=="-":
            number*=-1
            count+=1
            lst.pop(index)
        elif isinstance(lst[index],int) or isinstance(lst[index],float)or lst[index].isdigit():
            lst[index]*=number
            count=0
            if tilda_check:
                lst[index] = f"~{lst[index]}"
                tilda_check=0
            index+=1
        else:
            index+=1
    return lst
