def calcular_populacao_dodo(populacao_inicial):
    ano = 1600
    populacao_atual = populacao_inicial
    limite = populacao_inicial * 0.1

    while populacao_atual >= limite:
        nascimentos = populacao_atual * 0.01
        mortes = populacao_atual * 0.06
        populacao_atual += nascimentos - mortes

        print(f"{ano},{round(nascimentos)},{round(mortes)},{round(populacao_atual)}")
        ano += 1

def main():
    try:
        populacao_inicial = int(input())
        calcular_populacao_dodo(populacao_inicial)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()