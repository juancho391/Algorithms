def bubleSort(lista:list)->list:
    for j in range(len(lista)):
        for i in range(0,len(lista)-1):
            if lista[i] < lista[i+1]:
                continue
            else:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista
    
