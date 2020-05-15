#Programa que procura caracteres comuns a ambas strings
stringA = input("Informe a primeira String: ")
stringB = input("Informe a segunda String: ")
comum = []
for letra in stringB:
    resultado = stringA.lower().find(letra.lower())
    if resultado >=0:
        comum += letra
    resultado = -1

print("As letras em comum são:\n")
print("".join(comum))