# Programa que calcula a quantidade de dias, horas e minutos e os converte em segundos
dia = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

print(f"A quantidade de segundos correspondente é {(dia*24*3600)+(horas*3600)+(minutos*60)}")