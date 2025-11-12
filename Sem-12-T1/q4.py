def num_sorte(n):
    soma = 0
    for digito in n:
        soma += int(digito)
    return soma

def main():
    data = input().strip()
    print(num_sorte(data))
    
if __name__ == "__main__":
    main()