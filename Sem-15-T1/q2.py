def criando_tupla():
    temp = float(input().strip())
    tipo_temp = input().strip().upper()[0]
    return (temp, tipo_temp)

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def soma(temp_1, temp_2):
    valor1, esc1 = temp_1
    valor2, esc2 = temp_2

    if esc1 == esc2:
        return (round(valor1 + valor2, 4), esc1)

    if esc2 == 'C':
        valor1_convertido = fahrenheit_para_celsius(valor1) if esc1 == 'F' else valor1
        return (round(valor1_convertido + valor2, 4), 'C')

    else:  
        valor1_convertido = celsius_para_fahrenheit(valor1) if esc1 == 'C' else valor1
        return (round(valor1_convertido + valor2, 4), 'F')

def main():
    temp_1 = criando_tupla()
    temp_2 = criando_tupla()
    print(soma(temp_1, temp_2))

if __name__ == "__main__":
    main()
