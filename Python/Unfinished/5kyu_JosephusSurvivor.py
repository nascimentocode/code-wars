def josephus_survivor(n,k):
    list = []
    for i in range(1, n+1):
        list.append(i)

    return list   

print(josephus_survivor(7,3))