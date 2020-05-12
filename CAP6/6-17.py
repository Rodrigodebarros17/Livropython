produtoEncontrado = False
venda = []


estoque = {"tomate" : [1000, 2.30],
           "alface" : [500, 0.45],
           "batata" : [2001, 1.20],
           "feijão" : [100, 1.50]}

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
    
while True:
    produto = input("informe o produto (S para sair): ")
    if produto == "s":
        break
    for chave in estoque.items():
        if chave[0] == produto:
            produtoEncontrado = True
            break
    if produtoEncontrado:
        quantidade = int(input("Informe a quantidade vendida: "))
        venda.append([produto, quantidade])

    else:
        print("produto informado não encontrado\n")
        print("informe novamente")


total = 0
print(venda)
print("Vendas:\n")


for operação in venda:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo

print(f" Custo Total: {total:21.2f}\n")
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")

