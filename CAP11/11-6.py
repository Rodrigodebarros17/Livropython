import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        while True:
            produto = input("Qual produto gostaria de excluir?(enter para sair): ")
            if produto == "":
                break
            valor = input(f"Informe o novo valor para {produto}: ")
            cursor.execute("""update produtos 
                                set preco = ? where produto = ?
                                    """, (valor, produto))
        conexao.commit()
        print("Registros alterados: ", cursor.rowcount)
            

