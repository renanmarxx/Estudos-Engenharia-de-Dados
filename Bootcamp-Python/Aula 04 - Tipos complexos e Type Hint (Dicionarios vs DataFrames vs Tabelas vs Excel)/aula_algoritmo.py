lista_de_numeros: list = [40, 50, 60, 70, 0, -5000, -200, 50]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(lista_de_numeros)):
        for j in range(i+1, len(lista_de_numeros)):
            if lista_de_numeros[i] > lista_de_numeros[j]:
                lista_de_numeros[i], lista_de_numeros[j] = lista_de_numeros[j], lista_de_numeros[i]

    return nova_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)    
print(nova_lista)