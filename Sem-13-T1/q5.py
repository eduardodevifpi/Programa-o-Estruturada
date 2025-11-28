def criar_lista_um():
    lista = []
    for _ in range(25):
        numero = int(input().strip())
        lista.append(numero)
    return lista

def criar_lista_dois():
    lista = []
    for _ in range(25):
        numero = int(input().strip())
        lista.append(numero)
    return lista

def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada

def main():
    lista1 = criar_lista_um()
    lista2 = criar_lista_dois()
    todos = intercalar_listas(lista1, lista2)
    print(lista1)
    print(lista2)
    print(todos)

if __name__ == "__main__":
    main()
