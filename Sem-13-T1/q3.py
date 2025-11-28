def parte_a(n):
    if n == 0:
        print([])
        return []
    
    lista = []
    for _ in range(n):
        valor = float(input().strip())
        lista.append(valor)

    lista = lista[::-1]
    print(lista)
    return lista


def parte_b(n):
    if n == 0:
        print([])
        print("SEM NOTAS")
        return []

    notas = []
    for _ in range(n):
        nota = float(input().strip())
        notas.append(nota)

    media = sum(notas) / n

    print(notas)
    print(round(media, 1))

    return notas


def parte_c(n):
    if n == 0:
        print(0)
        print([])
        return []

    letras = []
    for _ in range(n):
        letra = input().strip()
        letras.append(letra)

    vogais = set("aeiouAEIOU")

    qtd_vogais = sum(1 for l in letras if l in vogais)
    consoantes = [l for l in letras if l not in vogais]

    print(qtd_vogais)
    print(consoantes)

    return letras


def main():
    n = int(input().strip())

    parte_a(n)
    parte_b(n)
    parte_c(n)


if __name__ == "__main__":
    main()
