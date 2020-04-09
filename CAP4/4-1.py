# Programa para indicar se houve multa
velocidade = int(input("Indique a velocidade em que você estava? "))

if velocidade <= 80:
    print("Você é um motorista consciente com a noção de velocidade!")

if velocidade > 80:
    print(f"Seu puto burro do caralho, passou de 80 Km/h, o valor da sua multa é R$ {(velocidade-80)*5}")