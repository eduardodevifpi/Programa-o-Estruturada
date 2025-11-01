def eh_letra_ou_numero(caractere):
    return caractere.isalpha() or caractere.isdigit()

def main():
    entrada = input().strip()
    print(eh_letra_ou_numero(entrada))
    
if __name__ == "__main__":
    main()