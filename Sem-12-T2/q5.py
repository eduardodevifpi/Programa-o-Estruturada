def main():
    x = int(input().strip())
    y = int(input().strip())


    if x > y:
        x, y = y, x

    for n in range(x, y + 1):
        if n > 1:  
            eh_primo = True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                print(n)
                
if __name__ == "__main__":
    main()
