numero = int(input("Digite o valor para verificação: "))

if numero > 2:
    contador = 0
    if numero % 2 != 0:
        contador = 3
        while contador < numero:
            if numero % contador !=0:
                contador = numero
    if contador == numero:
        print("Número é primo")
    else:
        print("Número não é primo")
else:
    print("Número é primo")

