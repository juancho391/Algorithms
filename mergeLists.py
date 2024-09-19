#import my buble sort method 

from bublesort import bubleSort

def mergeLists(lista1, lista2):
    for i in lista2:
        lista1.append(i)
    bubleSort(lista1)
    return lista1


lista1 = [1,2,4]
lista2 = [1,3,4]
print(mergeLists(lista1, lista2))
