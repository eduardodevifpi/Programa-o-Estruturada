def main():
    numero = int(input().strip())
    a = 0
    b = 1

    print(f"{a}, {b}", end='')

    for i in range(2, numero):
        c = a + b
        print(f", {c}", end='')
        a = b
        b = c

if __name__ == "__main__":
    main()
