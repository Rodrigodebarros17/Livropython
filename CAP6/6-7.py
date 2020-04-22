#Programa para verificar abertura e fechamento de parenteses
parenteses = input("Digite a sequencia de parenteses: ")
contador = 0
pilhaParenteses = []

while contador < len(parenteses):
    if parenteses[contador] == "(" :
        pilhaParenteses += "("
    elif parenteses[contador] == ")" :
        if len(pilhaParenteses) > 0 :
            del pilhaParenteses[0]
        else:
            print("Não possui fechamento adequado")
            break
    else:
        print("Você digitou um caractere errado")
        break
    contador += 1

print(f"{contador}, {len(pilhaParenteses)}")

if (contador == (len(parenteses))) and (len(pilhaParenteses) == 0):
    print("Fechamento adequado")
else:
    print("Fechamento incorreto")
