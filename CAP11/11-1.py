import sqlite3
conexao = sqlite3.connect("precos.db")
cursor = conexao.cursor()
cursor.execute('''
    create table produtos(
        produto text,
        preco float
    )
    ''')

while True:
    produto = input("Favor, informe o nome do produto(enter para sair do programa):")
    if produto == "":
        break
    preco = input("informe o preço do produto:")
    cursor.execute('''
        insert into produtos (produto, preco)
        values(?, ?)
        ''', (produto, preco))

conexao.commit()
cursor.close()
conexao.close()