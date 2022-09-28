def narcissistic(value):
    sum = 0
    for i in str(value):
        sum += pow(int(i), len(str(value)))

    return sum == value
