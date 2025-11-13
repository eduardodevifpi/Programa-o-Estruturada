def main():
    n = int(input().strip())
    H = 0.0

    for i in range(1, n + 1):
        H += 1 / i

    print(f"{H:.4f}")

if __name__ == "__main__":
    main()
