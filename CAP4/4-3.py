# Programa que define o maior e menor número
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
menor =  a
maior = a
if menor > b:
    menor = b
if menor > c:
    menor = c
if maior < b:
    maior = b
if maior < c:
    maior = c

print(f"O maior número é {maior} e o menor é {menor}")