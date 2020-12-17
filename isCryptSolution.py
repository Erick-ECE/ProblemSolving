#isCryptSolution
def isCryptSolution(crypt,solution):
    d= dict(solution) # maps a list to a dict
    table = str.maketrans(d)
    trans=[s.translate(table) for s in crypt]
    for i in trans:
        if len(i)>1 and i[0]=='0':
            return False
    trans = list(map(int, trans))
    if trans[0]+trans[1] == trans[2]:
        return True
    return False





#test#
c = ["SEND", "MORE",  "MONEY"]
sol= [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

print(isCryptSolution(c,sol))