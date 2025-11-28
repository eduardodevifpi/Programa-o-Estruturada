import numpy as np

def criar_lista():
    lista = []
    for _ in range(10):
        numero = int(input().strip())
        lista.append(numero)
    return lista

def soma(lista):
    return sum(lista)

def multiplicacao(lista):
    return np.prod(lista)

def main():
    lista_numeros = criar_lista()
    print(lista_numeros)
    print(soma(lista_numeros))
    print(multiplicacao(lista_numeros))
    
    
if __name__ == "__main__":
    main()