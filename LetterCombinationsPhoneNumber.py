def numcomb(s):
    numbers={
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }

    l=len(s)
    if l==1:
        return numbers[s]
    elif l==2:
        return [i+j for i in numbers[s[0]] for j in numbers[s[1]]]
    elif l==3:
        return [i+j+k for i in numbers[s[0]] 
                        for j in numbers[s[1]] 
                            for k in numbers[s[2]]]
    elif l==4:
        return [i+j+k+l for i in numbers[s[0]] 
                        for j in numbers[s[1]] 
                            for k in numbers[s[2]]
                                for l in numbers[s[3]]]
    else:
        return []

# prueba:
print(numcomb('23'))