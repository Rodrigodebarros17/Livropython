#Cálculo de juros simples
import time

depInicial = float(input("Digite o depósito inicial: "))
juros = float(input("Digite a taxa de juros: "))

ganhos = 0
contador = 1
depAtual = depInicial


while contador <= 24:
    ganhos = depAtual * (juros/100)
    depAtual = depAtual + ganhos
    print(f"O Saldo dos investimentos no mês {contador} é {depAtual:.2f}")
    contador = contador + 1
    time.sleep(0.5)

print(f"O total de ganhos no périodo foi {depAtual-depInicial:.2f}")