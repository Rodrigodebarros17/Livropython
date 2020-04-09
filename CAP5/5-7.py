# tabuada com início definido pelo usuário
numerotabuada = int(input("Digite o número para calcular tabuada: "))
inicioTabuada = int(input("Digite o número para início de cálculo de tabuada: "))

while inicioTabuada <= 10:
    print(f"{numerotabuada} x {inicioTabuada} = {numerotabuada*inicioTabuada}")
    inicioTabuada = inicioTabuada + 1