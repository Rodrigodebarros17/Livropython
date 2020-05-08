#Programa que retorna área de um triângulo
def calculoarea(altura, base):
    return (base*altura)/2

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

print(f"a área do triangulo é {calculoarea(altura, base)}")