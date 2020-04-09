# divisão usando subtração
# multiplicação com soma
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

resto = dividendo
contador = 0

while (resto >= divisor):
    resto = resto - divisor
    contador = contador + 1

print (f"{dividendo}/{divisor} = {contador} com resto {resto}")
