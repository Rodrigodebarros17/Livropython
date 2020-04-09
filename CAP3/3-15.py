#Cálculo de reduçao de tempo de vida de fumante
cigarrosDia = int(input("Quantos cigarros vc fuma por dia? "))
anos = int(input("Há quantos anos vc fuma? "))

print(f" você já perdeu {((anos*365*cigarrosDia)*10)/(24*60):f} dias da sua vida")