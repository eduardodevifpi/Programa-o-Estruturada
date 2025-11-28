def criando_lista():
    lista = []
    while True:
        n = int(input().strip())
        if n == 0:
            break
        lista.append(n)
    return lista

def soma_cumulativa(lista):
    cumulativa = []
    soma = 0
    for valor in lista:
        soma += valor
        cumulativa.append(soma)
    return cumulativa

def main():
    lista = criando_lista()
    print(soma_cumulativa(lista))   
    
if __name__ == "__main__":
    main()