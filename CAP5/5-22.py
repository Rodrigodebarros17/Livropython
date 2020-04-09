operacao = input("Digite a operação (+ para soma, - para subtração, * para multiplicação, / para divisão, ^ para potenciação, 0 para sair): ")

while operacao != "0":
    base = int(input("Digite o valor da tabuada: "))
    operando = 1
    if operacao == "+":
        while operando <= 10:
            print(f"{base} + {operando} = {base + operando}")
            operando += 1
    elif operacao == "-":
        while operando <= 10:
            print(f"{base} - {operando} = {base - operando}")
            operando += 1
    elif operacao == "*":
        while operando <= 10:
            print(f"{base} x {operando} = {base * operando}")
            operando += 1
    elif operacao == "/":
        while operando <= 10:
            print(f"{base} / {operando} = {base / operando}")
            operando += 1
    elif operacao == "^":
        while operando <= 10:
            print(f"{base} ^ {operando} = {base ** operando}")
            operando += 1
    else:
        print("Você digitou uma opção de operação incorreta")
    operacao = input("Digite a operação (+ para soma, - para subtração, * para multiplicação, / para divisão, ^ para potenciação, 0 para sair): ")


    
