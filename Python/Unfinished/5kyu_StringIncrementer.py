# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100

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