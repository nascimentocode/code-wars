def productFib(prod):
    fibonacci = []
    for i in range(prod+3):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append((fibonacci[i-1])+(fibonacci[i-2]))
            if fibonacci[i-1]*fibonacci[i-2] == prod:
                return [fibonacci[i-2], fibonacci[i-1], True]
            elif fibonacci[i-1]*fibonacci[i-2] > prod:
                return [fibonacci[i-2], fibonacci[i-1], False]