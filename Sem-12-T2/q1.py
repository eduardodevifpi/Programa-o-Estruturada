def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def main():
    numero = int(input().strip())
    print(fatorial(numero))
    
if __name__ == "__main__":
    main()