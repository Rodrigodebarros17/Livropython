# Programa para cálculo de valor de passagem
distancia = int(input("Por favor, informe a distância a ser percorrida: "))

if distancia <= 200:
    print(f" o valor da sua passagem é R$ {distancia*0.50}")

else:
     print(f" o valor da sua passagem é R$ {distancia*0.45}")
