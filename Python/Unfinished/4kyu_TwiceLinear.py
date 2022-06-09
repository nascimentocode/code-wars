def dbl_linear(n):
    u = [1]
    for x in u:
        if len(u) >= n:
            break
        # if u[-1] > 2*x+1:
        #     u.insert(u.index(u[-1]), 2*x+1)
        # else:
        #     u.append(2*x+1)
        u.append(2*x+1)
        u.append(3*x+1)

    return u[n]

print(dbl_linear(10))