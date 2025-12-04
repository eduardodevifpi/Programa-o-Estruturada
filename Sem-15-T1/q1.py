def criando_tupla():
    temp = float(input().strip())
    tipo_temp = input().strip().upper()[0]
    return (temp, tipo_temp)

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def maior(temp_1, temp_2):
    if temp_1[1] == temp_2[1]:
        if temp_1[0] > temp_2[0]:
            return temp_1
        else:
            return temp_2
    
    if temp_1[1] != temp_2[1]:
        if temp_1[1] == 'C':
            temp_1_f = celsius_para_fahrenheit(temp_1[0])
            if temp_1_f > temp_2[0]:
                return temp_1
            else:
                return temp_2
        else:
            temp_2_f = celsius_para_fahrenheit(temp_2[0])
            if temp_2_f > temp_1[0]:
                return temp_2
            else:
                return temp_1
        

def main():
    temp_1 = criando_tupla()
    temp_2 = criando_tupla()
    print(maior(temp_1, temp_2))
    

if __name__ == "__main__":
    main()

