# Programa para calcular gasto de energia elétrica
consumo = float(input("Digite a quantidade de Kw/h consumidos: "))
tipoConsumidor = input("Digite o tipo da instalação (I para industrias, R para residencias e C para comércios): ")

if tipoConsumidor == "R" or tipoConsumidor == "r":
    if consumo >= 500:
        print(f"O valor da sua conta é R$ {consumo*0.40}")
    else:
        print(f"O valor da sua conta é R$ {consumo*0.65}")

elif tipoConsumidor == "C" or tipoConsumidor == "c":
    if consumo <= 1000:
        print(f"O valor da sua conta é R$ {consumo*0.55}")
    else :
        print(f"O valor da sua conta é R$ {consumo*0.60}")

elif  tipoConsumidor == "i" or tipoConsumidor == "I":
    if consumo <= 5000:
        print(f"O valor da sua conta é R$ {consumo*0.55}")
    else :
        print(f"O valor da sua conta é R$ {consumo*0.60}")

else:
    print("O tipo de consumo informado não corresponde a nenhum existente")