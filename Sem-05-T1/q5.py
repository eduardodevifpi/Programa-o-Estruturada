def inverter_numero(numero):     
    
    if 1000 <= numero <= 9999:
        invertido = str(numero)[::-1]
        return invertido
    else:
        return False


def main():
    numero = int(input().strip())        
    resultado = inverter_numero(numero)
    print(resultado)

if __name__ == "__main__":
    main()
