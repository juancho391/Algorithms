def fibonnaci(n):
    a = 0
    b = 1
    lista = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            lista.append(c)
    return lista

print(fibonnaci(32))
