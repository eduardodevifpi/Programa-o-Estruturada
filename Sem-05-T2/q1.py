def eh_vogal(caractere):
    vogais = 'aeiou'
    return caractere in vogais

def main():
    entrada = input().strip().lower()
    print(eh_vogal(entrada))
    
if __name__ == "__main__":
    main()

