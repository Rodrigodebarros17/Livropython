import types

def printLista(L, ident = 0):
    print(ident * " ")
    for e, x in enumerate(L):
        if isinstance(type(x), list):
            printLista(ident + 1, L)
            ident += 1
            
        else:
            print(x)
            del L[e] 

printLista([2, [2,2], [3,3,3,3]])  


