def conceito_nota(nota):
    if nota >= 8.5:
        return "A"
    elif nota >= 7.0:
        return "B"
    elif nota >= 5.0:
        return "C"
    elif nota >= 4.0:
        return "D"
    else:
        return "E"

def main():    
    while True:
        nota = float(input().strip())
        
        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida.")
    
    print(conceito_nota(nota))
    
if __name__ == "__main__":
    main()
