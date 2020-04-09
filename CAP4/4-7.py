# calculadora
print("Programa calculdora")
a = float(input("digite o primeiro operando: "))
b = float(input("Digite o segundo operando: "))
operação = input("Digite o simbolo da operação desejada (+ para soma, * para multiplicação, / para divisão, - para subtração e ^ para exponenciação): ")

if operação == "+":
    print(f"O resultado da soma é {a+b}")

elif operação == "*":
    print(f"O resultado da multiplicação é {a*b}")

elif operação == "/":
    if b == 0:
        print("Não é possível realizar divisão por 0")
    else:
        print(f"O resultado da multiplicação é {a/b}")

elif operação == "-":
    print(f"O resultado da subtração é {a-b}")

elif operação == "^":
    print(f"O resultado da exponenciação é {a**b}")

else:
    print("O operando digitado não é válido, execute novamente o programa indicando a operação correta")

