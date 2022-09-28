def solution(s):
    listS = []  
    for i in range(0, len(s), 2):
        if len(s[i:i+2]) == 1:
            listS.append(s[i] + '_')
        else:
            listS.append(s[i:i+2])

    return listS
