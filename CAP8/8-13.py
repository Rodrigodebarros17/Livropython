# adivinhando o número
import random
n = random.randint(1,10)
x = int(input("Digite um número entre 1 e 10: "))
chances = 3
while chances > 0:
    if x == n:
        print("Parabéns, vc acertou:")
        break
    else:
        chances -= 1
        print(f"Você errou, voçe tem mais {chances} chances ")
        x = int(input("Qual seu novo palpite: "))