def resposta(opcao):
    if opcao == 1:
        return "1 - Olá. Como vai?"
    elif opcao == 2:
        return "2 - Vamos estudar mais."
    elif opcao == 3:
        return "3 - Meus Parabéns!"
    else:
        return "Opção inválida."

def main():
    while True:
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")

        opcao = int(input().strip())

        if opcao == 0:
            print("0 - Fim de serviço.")
            break

        print(resposta(opcao))

if __name__ == "__main__":
    main()
