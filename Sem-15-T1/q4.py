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


def main():
    limite = int(input().strip())
    cidades = carrega_cidades()

    print(f"CIDADES COM MAIS DE {limite} HABITANTES:")
    for uf, cod, nome, dia, mes, pop in cidades:
        if pop > limite:
            print(f"IBGE: {cod} - {nome}({uf}) - POPULAÇÃO: {pop}")

if __name__ == "__main__":
    main()