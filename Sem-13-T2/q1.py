def criando_lista():
    lista = []
    while True:
        n = int(input().strip())
        if n == 0:
            break
        lista.append(n)
    return lista

def multiplicando(numero, lista):
    produto = []
    for valor in lista:
        produto.append(valor * numero)
    return produto

def main():
    lista = criando_lista()
    numero = int(input().strip())
    print(multiplicando(numero, lista))
    
if __name__ == "__main__":
    main()