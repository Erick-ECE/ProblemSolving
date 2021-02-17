# Permutaciones sin repetición
#input= "abc"
#output= ["abc","bca","cab","acb","cba","bac"]

# funcion auxiliar
def multi_insert(elem, lista):
    return [lista[:i]+[elem]+lista[i:]
     for i in range(len(lista)+1)]


def permutation(lista):
    if len(lista) == 0:
        return [[]]
    return sum([multi_insert(lista[0],s) for s in permutation(lista[1:])] , [] )

permutation(['a','b','c'])