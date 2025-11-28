def criar_lista():
    lista = []
    for _ in range(50):
        numero = float(input().strip())
        lista.append(numero)
    return lista

def medias_altas(lista):
    indices = []
    for i in range(len(lista)):
        if lista[i] >= 6:
            indices.append(i)  
    return indices

def main():
    lista = criar_lista()
    altas = medias_altas(lista)
    print(altas)
    
if __name__ == "__main__":
    main()
