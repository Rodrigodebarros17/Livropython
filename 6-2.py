# programa que gera uma terceira lista a partir de duas que são lidas
x=[]
z=[]
numero = 0

while True:
    numero = float(input("Digite um elemento da primeira lista (0 para sair): "))
    if numero == 0:
        break
    x += [numero]

while True:
    numero += float(input("Digite um elemento da segunda lista (0 para sair): "))
    if numero == 0:
        break
    z += [numero]

print (f" a soma das listas é {x + z}")

