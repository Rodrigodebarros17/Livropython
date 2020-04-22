# Programa simulação de uma fila de banco
últimoa = 10
últimob = 10
filaa = list(range(1, últimoa + 1))
filab = list(range(1, últimob + 1))
while True:
    print(f"Existem {len(filaa)} clientes na fila A")
    print(f"Existem {len(filab)} clientes na fila B")
    print(f"Fila Atual A: {filaa}")
    print(f"Fila Atual B: {filab}")
    print("Digite F para adicionar um cliente ao fim da fila A, ")
    print("Digite G para adicionar um cliente ao fim da fila B, ")
    print("ou A para realizar o atendimento na fila A, S para sair")
    print("ou B para realizar o atendimento na fila B, S para sair")
    operacao = input ("Operação (F, G, A, B ou S): ")
    contador = 0    
    while contador < len(operacao):
        if operacao[contador] == "A":
            if len(filaa) > 0:
                atendido = filaa.pop(0)
                print(f"Cliente {atendido} da Fila A atendido")
            else:
                print("Fila vazia! Ninguém para atender")
        elif operacao[contador] == "B":
            if len(filab) > 0:
                atendido = filab.pop(0)
                print(f"Cliente {atendido} da Fila B atendido")
            else:
                print("Fila vazia! Ninguém para atender")
        elif operacao[contador] == "F":
            últimoa += 1 # Incrementa novo cliente
            filaa.append(últimoa)
            print("Cliente Adicionado a Fila A")
        elif operacao[contador] == "G":
            últimob += 1 # Incrementa novo cliente
            filab.append(últimob)
            print("Cliente Adicionado a Fila B")
        elif operacao[contador] == "S":
            break
        else:
            print("Operação inválida, digite apenas F, A ou S!")
        
        contador += 1

    if operacao[contador] == "S":
        break
    