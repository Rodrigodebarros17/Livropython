#Cálculo de desconto de mercadoria
valor = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

print(f"O valor final da mercadoria é {valor-(valor*(desconto/100))}")