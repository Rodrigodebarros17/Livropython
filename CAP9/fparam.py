import sys
print(f"Numero de parametro: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")
