def calcular(a, b, c):
    resultado = (2 * a) + (5 * b) - c
    return resultado

def main():
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    resultado = calcular(a, b, c)
    print(resultado)
     
if __name__ == "__main__":
    main()
