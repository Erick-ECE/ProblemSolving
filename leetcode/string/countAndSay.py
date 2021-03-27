#count and say

#The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

#countAndSay(1) = "1"
#countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

def conuntAndSay(n):
    base= "1"
    for i in range(n-1):
        base=calculaSig(base)
    return base



def calculaSig(num): #"111221"
    if num=="1":
        return "11"
    temp=""
    last=num[0]
    count=1
    for i in range(1,len(num)):
        if num[i]==last:
            count+=1
        if num[i]!=last:
            temp+=str(count)+last
            last=num[i]
            count=1
        if i==len(num)-1:
            temp+=str(count)+num[i]
    return temp

conuntAndSay(1)
conuntAndSay(10)=="13211311123113112211"
