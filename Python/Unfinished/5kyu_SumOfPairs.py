l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

def sum_pairs(ints, s):
    temp = []
    for i in range(len(ints)):  
        for j in range(len(ints)):
            if j != i:
                if ints[i]+ints[j]==s:
                    if not [j, i] in temp:
                        temp.append([i, j])

    if len(temp) == 1:
        return temp[0]
    else:
        menor = temp[0][1] - temp [0][0]
        result = temp[0]
        for i in range(1, len(temp)) :
            if (temp[i][1] - temp[i][0]) < menor:
                result = temp[i]

        return result