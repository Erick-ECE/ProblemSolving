def minRemoveToMakeValid(s):
    cp=''
    op=''
    balance=0
    for i in s: # first loop to catch excess of close parenthesis
        if i == '(':
            balance+=1
        elif i ==')':
            if balance==0:
                continue
            balance-=1
        cp += i
        
    for j in cp[::-1]: # to catch excess open parenthesis
        if j == '(' and balance>0:
            balance -= 1
            continue
        op+=j
    return op[::-1]