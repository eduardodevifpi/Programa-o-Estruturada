def valores(codigo, quantidade):
    if codigo == 'H':
        return 5.50 * quantidade
    elif codigo == 'C':
        return 6.80 * quantidade
    elif codigo == 'M':
        return 4.50 * quantidade
    elif codigo == 'A':
        return 7.00 * quantidade
    elif codigo == 'Q':
        return 4.00 * quantidade
    else:
        return 0

def main():
    soma = 0
    
    while True:
        print("""CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5.50
C       Cheeseburger    6.80
M       Misto Quente    4.50
A       Americano       7.00
Q       Queijo Prato    4.00
X       PARA TOTAL DA CONTA""")

        codigo = input().strip().upper()

        if codigo == 'X':
            break

        quantidade = int(input().strip())

        soma += valores(codigo, quantidade)
        
    print(f"{soma:.2f}")
    
if __name__ == "__main__":
    main()
