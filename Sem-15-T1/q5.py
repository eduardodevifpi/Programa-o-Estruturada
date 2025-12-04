import csv

def carrega_cidades():
    cidades = []
    with open("cidades.csv", encoding="utf-8") as f:
        leitor = csv.reader(f, delimiter=';')
        next(leitor)  
        for linha in leitor:
            uf = linha[0]
            cod = int(linha[1])
            nome = linha[2]
            dia = int(linha[3])
            mes = int(linha[4])
            pop = int(linha[5])
            cidades.append((uf, cod, nome, dia, mes, pop))
    return cidades

def nome_mes(m):
    meses = [
        "", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return meses[m]


def main():
    mes = int(input().strip())
    limite = int(input().strip())

    cidades = carrega_cidades()

    print(f"CIDADES COM MAIS DE {limite} HABITANTES E ANIVERSÁRIO EM {nome_mes(mes).upper()}:")
    for uf, cod, nome, dia, m, pop in cidades:
        if pop > limite and m == mes:
            print(f"{nome}({uf}) tem {pop} habitantes e faz aniversário em {dia} de {nome_mes(mes)}.")

if __name__ == "__main__":
    main()