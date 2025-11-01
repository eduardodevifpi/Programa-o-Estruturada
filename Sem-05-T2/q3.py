def eh_consoante(caractere):
    vogais = 'aeiou'
    return caractere.isalpha() and caractere.lower() not in vogais


def main():
    entrada = input().strip()
    print(eh_consoante(entrada))
    
if __name__ == "__main__":
    main()