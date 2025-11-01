def eh_letra(caractere):
    return caractere.isalpha()


def main():
    entrada = input().strip()
    print(eh_letra(entrada))
    
if __name__ == "__main__":
    main()