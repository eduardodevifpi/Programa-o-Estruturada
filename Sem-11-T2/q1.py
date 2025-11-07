def main():
    soma = 0
    
    while True:
        numero = int(input().strip())
        if numero == 0:
            break
        soma += numero
        
    print(soma)

if __name__ == "__main__":
    main()