# Imprimir impares até tal número
fim = int(input("Digite o número final(acima de 30): "))

x = 0

while x <= fim:
    if (x % 3) == 0:
        print (x)
    x = x + 1
