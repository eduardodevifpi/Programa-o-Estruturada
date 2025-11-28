def criar_lista():
    lista = []
    for _ in range(100):
        numero = int(input().strip())
        lista.append(numero)
    
    lista.sort()     
    return lista     

def nova_lista(lista):
    resultado = []
    for i in range(len(lista)):
        if i % 2 == 0:  
            resultado.append(lista[i] * 3)
        else:          
            resultado.append(lista[i] * 5)
    return resultado
    
def main():
    lista = criar_lista()
    print(nova_lista(lista))

if __name__ == "__main__":
    main()
