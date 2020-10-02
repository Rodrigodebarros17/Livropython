import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from produtos")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Produto: {resultado[0]}\nValor: R${resultado[1]}\n")
