notas = [0,0,0,0,0,0,0]
x = 0
soma = 0

while x < 7:
    notas[x] = float(input(f"Nota {x}: "))
    x += 1

x = 0

while x < 7:
    soma += notas[x]
    x += 1

print(f"a média do aluno é {soma/x:.2f}")