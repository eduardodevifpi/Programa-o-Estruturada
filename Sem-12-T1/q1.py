def calculo(distancia_inicial):
    diferenca = 10 - 1
    tempo = distancia_inicial / diferenca
    return round(tempo)


def main():
    distancia_inicial = int(input().strip())
    print(calculo(distancia_inicial))
    
if __name__ == "__main__":
    main()
    
