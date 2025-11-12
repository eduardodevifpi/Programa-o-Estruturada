def calculo(pop_a, pop_b):
    taxa_a = 0.02
    taxa_b = 0.03
    anos = 0
    
    while pop_b < pop_a:
        pop_a += pop_a * taxa_a
        pop_b += pop_b * taxa_b
        anos += 1
        
    return anos


def main():
    pop_a = float(input().strip())
    pop_b = float(input().strip())
    
    if pop_a > pop_b:
        num_um = pop_a
        num_dois = pop_b
    else:
        num_um = pop_b
        num_dois = pop_a
    
    anos = calculo(num_um, num_dois)
    print(anos)


if __name__ == "__main__":
    main()
