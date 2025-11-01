def minutagem(minutos_totais):
    horas = minutos_totais // 60
    minutos = minutos_totais % 60
    return horas, minutos

def main():
    minutos = int(input().strip())
    horas, minutos_restantes = minutagem(minutos)
    print(f'{horas}:{minutos_restantes}')
    
if __name__ == "__main__":
    main()