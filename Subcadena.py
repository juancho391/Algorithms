def buscar_subcadena(cadena, subcadena):
    n = len(cadena)
    m = len(subcadena)
    ocurrencias = []
    for i in range (n - 1):
        j = 0
        while j < m:
            if cadena[i + j] != subcadena[j]:
                break
            j += 1
        if j == m:
            ocurrencias.append(i)
    return ocurrencias


cadena = "abracadabra"
subcadena = "abra"

print(buscar_subcadena(cadena, subcadena))
