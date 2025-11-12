def calculo(preco_carro):
    poupanca = 10000.0
    rendimento = 0.007 
    aumento_carro = 0.004
    meses = 0
    
    while poupanca < preco_carro: 
        poupanca += poupanca * rendimento
        preco_carro += preco_carro * aumento_carro
        meses += 1
        
    return meses

def main():
    preco_carro = float(input().strip())
    print(calculo(preco_carro))
    
if __name__ == "__main__":
    main()