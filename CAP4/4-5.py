# Programa para calcular o aumento de salário usando else
salario = float(input("Por favor digite o salário: "))
if salario > 1250:
    salario = salario * 1.10

else:
    salario = salario * 1.15

print(f"Seu novo salário é {salario:.2f}")