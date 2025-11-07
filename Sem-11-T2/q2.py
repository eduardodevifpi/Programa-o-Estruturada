def main():
    pessoas = 0
    soma = 0
    maior_idade = 0
    menor_idade = None
    
    while True:
        idade = int(input().strip())
        if idade == 0:
            break
        pessoas = pessoas + 1
        soma = soma + idade
        if idade > maior_idade:
            maior_idade = idade
            
        if menor_idade is None or idade < menor_idade:
            menor_idade = idade
            
    print(pessoas)
    print(f"{soma / pessoas:.2f}")
    print(menor_idade)
    print(maior_idade)

if __name__ == "__main__":
    main()