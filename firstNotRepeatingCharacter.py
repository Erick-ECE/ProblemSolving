# first solution # works! but slow
s = "abacabadcd"
ls= [s.count(x) for x in s]
if 1 in ls:
    print(s[ls.index(1)])
else:
    print("_")

# second solution (faster?) # not faster!
def firstRep(s):
    for i in s:
        if s.count(i) == 1:
            return i 
        else:
            pass
    return "_"

firstRep(s)

# third solution (faster?)
s = "abacabadcdsw"
ls= {x:s.count(x) for x in s}
if 1 in ls:
    print(s[ls.index(1)])
else:
    print("_")


#### 4th without usin count()
def firstNoRep(s):
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for j in s:
        if d[j] == 1:
            return j
    return "_"

s = "abacabad"
firstNoRep(s)

## Gladin's solution
from collections import defaultdict

def firstNotRepeatingCharacter(s):
    d = defaultdict(int)
    for x in s:
        d[x] += 1
    for x in s:
        if d[x] == 1:
            return x
    return '_'

s = "abacabad"  
firstNotRepeatingCharacter(s)

# like the 4th solution
def firstNotRepeatingCharacter(s):
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for j in s:
        if d[j] == 1:
            return j
    return "_"

# codeSignal solution (Awsome!
def firstNotReoetingChar(s):
    for i in s:
        if s.index(i) == s.rindex(i):
            return i
    return "_"

### Test:
ss = "abacabad"

print(firstNotReoetingChar(ss))

