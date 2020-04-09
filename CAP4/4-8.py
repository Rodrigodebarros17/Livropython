# Programa para aprovação de empréstimo

salário = float(input("Por favor, digite o valor do seu salário: "))
valorCasa = float(input("Por favor, digite o valor da casa: "))
anos = int(input("Por favor, digite a quantidade de anos que gostaria de quitar o empréstimo: "))

valorPrestacao = valorCasa/(anos*12)

if valorPrestacao > (salário*0.30):
    print("Não podemos aprovar o seu empréstimo")

else:
    print("O seu empréstimo foi aprovado")