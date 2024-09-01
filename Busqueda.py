lista = ["a","b","c","d","e","f","g"]


def busquedaSecuencial(lista,objetivo:str)->int:
    for i in range(0,len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

objetivo = "z"
resultado = busquedaSecuencial(lista,objetivo=objetivo)
if resultado != -1:
    print(f"El elemento {objetivo} fue encontrado en la posicion {resultado}")
else:
    print(f"El elemento {objetivo} no fue encontrado en la lista {lista}")
            

