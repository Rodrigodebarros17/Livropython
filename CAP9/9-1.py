#Leitura de arquivos
import sys
with open(sys.argv[1], "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)