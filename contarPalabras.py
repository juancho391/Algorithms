def contarPalabras(texto):
    palabras_contadas = {}
    lista_palabras = texto.split()
    for palabra in lista_palabras:
        if palabra in palabras_contadas:
            palabras_contadas[palabra.lower()] += 1
        else:
            palabras_contadas[palabra.lower()] = 1

    return palabras_contadas


print(contarPalabras("Hola como estas me contaron que estas con camilA hola camila"))
