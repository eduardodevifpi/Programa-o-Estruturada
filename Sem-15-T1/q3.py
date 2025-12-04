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
    dia = int(input().strip())
    mes = int(input().strip())
    cidades = carrega_cidades()

    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {nome_mes(mes).upper()}:")
    for uf, cod, nome, d, m, pop in cidades:
        if d == dia and m == mes:
            print(f"{nome}({uf})")

if __name__ == "__main__":
    main()
