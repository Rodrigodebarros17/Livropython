#Cálculo de aluguel de carro
dias = int(input("Digite a quantidade de dias que permaneceu com o carro: "))
quilometros = float(input("Digite a quantidade de quilometros percorridos: "))

print(f"O valor a ser pago é {(dias*60)+(quilometros*0.15):.2f}")