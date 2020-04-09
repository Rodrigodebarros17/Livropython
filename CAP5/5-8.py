# multiplicação com soma
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

x = 1
valorFinal = 0

while x <= primeiroNumero:
    valorFinal = valorFinal + segundoNumero
    x = x + 1

print(f"{primeiroNumero} x {segundoNumero} = {valorFinal}")