def criando_lista(n):
    lista = []
    for _ in range(n):
        valor = input().strip()
        try:
            valor = float(valor)
        except:
            pass
        lista.append(valor)
    return lista

def esta_ordenado(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def main():
    n = int(input().strip())
    lista = criando_lista(n)

    if esta_ordenado(lista):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")


if __name__ == "__main__":
    main()
