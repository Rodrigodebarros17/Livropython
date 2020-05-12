#Programa para validar strings
def comparastringlista(stringv, L):
    p = -1
    stringl = "".join(L)
    p = stringl.find(stringv)
    if p >=0:
        return True
    else:
        return False

resultado = comparastringlista("dri", ["d","r","i"])
print(resultado)

    