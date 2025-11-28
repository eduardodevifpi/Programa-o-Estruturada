def criar_lista():
    lista = []
    for _ in range(20):
        numero = int(input().strip())
        lista.append(numero)
    return lista

def numeros_pares(lista):
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    return pares

def numeros_impares(lista):
    impares = []
    for n in lista:
        if n % 2 != 0:
            impares.append(n)
    return impares


def main():
    lista = criar_lista()
    print(lista)
    pares = numeros_pares(lista)
    impares = numeros_impares(lista)
    print(pares)
    print(impares)

if __name__ == "__main__":
    main()
