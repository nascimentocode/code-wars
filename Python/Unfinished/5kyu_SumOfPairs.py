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

    print(temp)
    if len(temp) == 1:
        return temp[0]
    else:
        # menor = temp[0]
        for i in temp :
            print(i)

# print(sum_pairs(l1, 8))
# print(sum_pairs(l2, -6))
# print(sum_pairs(l3, -7))
print(sum_pairs(l4, 2))
# print(sum_pairs(l5, 10))
# print(sum_pairs(l6, 8))
# print(sum_pairs(l7, 0))
# print(sum_pairs(l8, 10))