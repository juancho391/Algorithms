# el algoritmo de ordenamiento por inserción es un método simple pero eficiente para ordenar 
# una lista de elementos. Funciona de manera similar a cómo muchas 
# personas ordenan cartas de juego en sus manos: tomando una carta a la vez e insertándola en
# su lugar correcto en la mano ordenada.
# Imagina que tienes una mano de cartas
# desordenadas frente a ti. Comienzas con la segunda
# carta y la comparas con la primera. Si la segunda
# carta es más pequeña, la insertas antes de la primera
# carta; de lo contrario, la dejas donde está. Luego, pasas
#  a la tercera carta y la insertas en su posición
# correcta entre las dos cartas anteriores. Repites este proceso con cada carta restante, siempre
# asegurándote de que todas las cartas a la izquierda estén ordenadas.
# Este proceso continúa hasta que todas las cartas estén en su posición correcta 
# y la mano esté completamente ordenada.
# En términos más técnicos, el algoritmo de ordenamiento por inserción funciona 
# recorriendo la lista desde el segundo elemento hasta el último. En cada paso, el algoritmo
#  compara el elemento actual con los elementos anteriores y lo inserta en la posición correcta entre
#  ellos. Este proceso se repite hasta que todos los elementos están en su lugar correcto.
# Una de las ventajas del algoritmo de ordenamiento por inserción es su simplicidad y su eficiencia 
# para listas pequeñas o casi ordenadas. Sin embargo, puede volverse más lento en listas
#  más grandes debido a su complejidad cuadrática O(n^2). Apesar de esto, sigue siendo útil 
# en muchas situaciones y es ampliamente utilizado en la práctica.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        iterador = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > iterador:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = iterador
    return lista


lista = [13,5,16,17,20,2,3,4]

print(insertion_sort(lista))