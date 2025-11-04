def main():
    primeiro_numero = True

    while True:
        numero = int(input().strip())

        if numero == 0:
            break  

        if primeiro_numero:
            maior = numero
            menor = numero
            primeiro_numero = False
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

    if primeiro_numero:
        print("Nenhum número foi digitado.")
    else:
        print(maior)
        print(menor)

if __name__ == "__main__":
    main()