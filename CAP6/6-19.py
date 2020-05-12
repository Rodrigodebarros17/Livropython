#Programa para comparar listas
a = list(range(10))
b = list(range(15))

print("valores somente em a")
print(a-b)

print("valores somente em b")
print(b-a)

print("valores comuns")
print(set(a-b)(b-a))

print("elementos não repetidos")
print(set(a,b))

print("lista elementos da primeira não repetidos segunda")
print(a-set(b))





