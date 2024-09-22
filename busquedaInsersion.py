#buscamos un elemento en la lista devolvemos su posicion y si no esta devolvemos la posicion 
#si se insertara en orden
def searchInsert(lista:list[int], target:int) -> int:
    posicion = len(lista)
    for i in range(len(lista)):
        if lista[i] == target:
            posicion = i
            break
        elif lista[i] > target:
            posicion = i
            break
    return posicion


print(searchInsert([1,2,3,4,5],3))
