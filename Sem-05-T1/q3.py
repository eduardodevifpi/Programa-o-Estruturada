def calcular_preco(preco, percentual):
    aumento = preco + (preco * percentual / 100)
    desconto = preco - (preco * percentual / 100)
    return aumento, desconto


def main():
    preco = float(input().strip())
    percentual = float(input().strip())
    aumento, desconto = calcular_preco(preco, percentual)
    print(f"{aumento:.2f}")
    print(f"{desconto:.2f}")
    
if __name__ == "__main__":
    main()