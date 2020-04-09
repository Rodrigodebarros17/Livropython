# programa que gera uma terceira lista a partir de duas que são lidas, sem repetição
x=[]
z=[]
count = 0
countxz = 0
novalista=[]
numero = 0

while True:
    numero = float(input("Digite um elemento da primeira lista (0 para sair): "))
    if numero == 0:
        break
    x += [numero]

while True:
    numero = float(input("Digite um elemento da segunda lista (0 para sair): "))
    if numero == 0:
        break
    z += [numero]

while count < len(x):
    valorAtual = x[count]
    countxz = 0
    while countxz < len(novalista):
        if valorAtual == novalista[countxz]:
            valorAtual += 1
            break
        countxz += 1
    if valorAtual == x[count]:
        novalista += [valorAtual]
    count += 1 

count = 0

while count < (len(z)):
    valorAtual = z[count]
    countxz = 0
    while countxz < len(novalista):
        if valorAtual == novalista[countxz]:
            valorAtual += 1
            break
        countxz += 1
    if valorAtual == z[count]:
        novalista += [valorAtual]
    count += 1 

print (f" a soma das listas é {novalista}")