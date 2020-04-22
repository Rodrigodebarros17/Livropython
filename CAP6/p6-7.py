# Programa simulação de uma fila de banco
último = 10
fila = list(range(1, último + 1))
while True:
    print(f"Existem {len(fila)} clientes na fila")
    print(f"Fila Atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila, ")
    print("ou A para realizar o atendimento, S para sair")
    operacao = input ("Operação (F, A ou S): ")
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender")
    elif operacao == "F":
        último += 1 # Incrementa novo cliente
        fila.append(último)
    elif operacao == "S":
        break
    else:
        print("Operação inválida, digite apenas F, A ou S!")        
