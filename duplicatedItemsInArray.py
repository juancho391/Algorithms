def removeDuplicate(lista):
    listAux = []
    for i in lista:
        if i not in listAux:
            listAux.append(i)
    return listAux


lista = [0,0,0,1,2,3,3,4,4,4,4,5,6,7,8,9,9,9,10]

print(removeDuplicate(lista))


