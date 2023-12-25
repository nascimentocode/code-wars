def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += pow(int(i), p)
        p+=1

    if sum%n == 0:
        return sum/n
    else:
        return -1
