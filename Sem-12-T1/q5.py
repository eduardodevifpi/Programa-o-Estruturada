def main():
    pop_inicial = int(input().strip())

    populacao = float(pop_inicial)
    ano = 1600

    while populacao >= 0.1 * pop_inicial:
        nascimentos = populacao * 0.01
        mortes = populacao * 0.06
        populacao = populacao - mortes + nascimentos

        
        print(f"{ano},{int(nascimentos)},{int(mortes)},{int(populacao)}")

        ano += 1


if __name__ == "__main__":
    main()
