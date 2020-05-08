#Como não escrever uma função - Consertando
def soma(L):
    total = 0
    x = 0
    for e in L:
        total += e
    return total
L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20]))