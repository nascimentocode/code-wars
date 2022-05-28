def descending_order(num):
    # listOrderReverse = sorted(str(num), reverse=True)
    # numReverse = "".join(listOrderReverse)

    # ↑ - faz a mesma função que as linhas acima mas em 1 única linha
    return int("".join(sorted(str(num), reverse=True)))