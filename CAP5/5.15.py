# Caixa registradora

#códigos
cod1 = 0.50
cod2 = 1
cod3 = 4
cod5 = 7
cod9 = 8

valorCompra = 0

while True:
    codigoProd = int(input("Digite o Código do Produto (Digite 0 para finalizar): "))
    if codigoProd == 0:
        break
    elif codigoProd == 1:
        valorCompra += cod1
    elif codigoProd == 2:
        valorCompra += cod2 
    elif codigoProd == 3:
        valorCompra += cod3
    elif codigoProd == 5:
        valorCompra += cod5
    elif codigoProd == 9:
        valorCompra += cod9
    else:
        print("Código Inexistente")

print(f"O valor total da compra é {valorCompra}")