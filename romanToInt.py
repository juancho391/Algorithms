
def romanos_enteros(self,cadena):
    lista = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for caracter in cadena:
        if caracter not in lista:
            return "Numero romano invalido"
    diccionarioNumeros = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    anterior = 0
    total = 0
    for caracter in range(0,len(cadena)):
        if diccionarioNumeros[cadena[caracter]] > anterior:
            actual = diccionarioNumeros[cadena[caracter]]
            resta = actual - (2*anterior)
            total +=resta
        else:
            total += diccionarioNumeros[cadena[caracter]]
        anterior = diccionarioNumeros[cadena[caracter]]
    return total 

print(romanos_enteros("MCMXCIV"))


