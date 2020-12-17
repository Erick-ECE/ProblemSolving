# find the words that match each other
def commonWords(a,b):
    aS = {s.lower() for s in a}
    bS = {s.lower() for s in b}
    return list(aS & bS)


# pruebas:
lista1= ['Juan', 'erick', 'pedro', 'Andy', 'juan','Erick']
lista2= ['Andy','juAn', 'Mike', 'Torta','cinthia']


print(' '.join(commonWords(lista1,lista2)))

def diffWords(a,b):
    aS={s.lower() for s in a}
    bS={s.lower() for s in b}
    return list(aS^bS)

print(' '.join(diffWords(lista1,lista2)))

