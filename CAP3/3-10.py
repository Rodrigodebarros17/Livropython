#Cálculo de aumento de salário
salário = float(input("Digite o valor do salário: "))
aumento = float(input("Digite o percentual de aumento: "))

print(f"O valor final do salário é {salário+(salário*(aumento/100))}")