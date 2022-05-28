def narcissistic(value):
    # valueV = []
    # for i in str(value):
    #     valueV.append(int(i))

    # ↑ - faz mesma função que a linha abaixo
    vetorValue = [int(i) for i in str(value)]

resultado = narcissistic(256)