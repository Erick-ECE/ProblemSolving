# almost increasing secuence

def ais(sec):
    flag=False
    last=prev= float('-inf')
    for elem in sec:
        if elem<=last:
            if flag:
                return False
            flag= True
            if elem<=prev:
                prev=last
            elif elem>prev:
                prev=last=elem #[1, 2, 3, 4]
        else:
            prev=last
            last=elem
    return True


section=[1,2,1,2]

ais(section)



         