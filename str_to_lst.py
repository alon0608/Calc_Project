def splitter(expression):
    """the function gets string and convert it into a list,
     every number takes place in the list and every operator as well. """
    final_list=[]
    current=""
    counter=0
    for char in expression:
        #check if char is number and handle it
        if char.isdigit() or char=="." or(char=="-" and current=="") or(char=="~" and current=="") or(char=="!" ):
            current+=char
        else:
            #if current is not empty final_list.append(current).
            if current:
                final_list.append(current)
                current=""
            #delete spaces
            if char!=" ":
                final_list.append(char)