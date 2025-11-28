def criando_lista(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i)
    return lista

def inverter_lista(lista):
    invertida = []
    for valor in lista:
        invertida.insert(0, valor)
    return invertida

def lista_zeros(n):
    return [0] * n

def ler_lista(n):
    lista = []
    for _ in range(n):
        valor = int(input().strip())
        lista.append(valor)
    return lista

def main():
    n = int(input().strip())
    print(lista_zeros(n))

    lista_numeros = criando_lista(n)
    print(lista_numeros)

    lista_usuario = ler_lista(n)
    print(lista_usuario)

    lista_usuario2 = ler_lista(n)
    print(inverter_lista(lista_usuario2))


if __name__ == "__main__":
    main()
