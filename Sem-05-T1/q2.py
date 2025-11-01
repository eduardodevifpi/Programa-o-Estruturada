def area_e_perimetro(lado):
    area = lado * lado
    perimetro = 4 * lado
    return area, perimetro

def main():
    lado = float(input().strip())
    area, perimetro = area_e_perimetro(lado)
    print(f"{area:10.4f}")      
    print(f"{perimetro:10.4f}")

if __name__ == "__main__":
    main()