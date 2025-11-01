def eh_simbolo(caractere):
    return not (caractere.isalpha() or caractere.isdigit())

def main():
    entrada = input().strip()
    print(eh_simbolo(entrada))
    
if __name__ == "__main__":
    main()