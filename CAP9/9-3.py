#lendo pares e impares
with open("impares.txt", "r") as impares, open("pares.txt", "r") as pares, open("pareseimpares.txt", "w") as pareseimpares:
    for s in pares.readlines():
        pareseimpares.write(s)
        for p in impares.readlines():
            if int(p) > int(s):
                pareseimpares.write(p)
                p = 0
                break
            