def increment_string(strng):
    n = ''
    for i in strng:
        if i.isdigit():
            n+=i
            strng = strng.replace(i, '')

    if n == '':
        strng += '1'
    else:
        if n[-1]+n[-2] == "99":
            strng+=n.replace("99", '')+"100"
        else:
            aux = n[-1]
            strng+=n.replace(aux, '')+str(int(aux)+1)

    return strng