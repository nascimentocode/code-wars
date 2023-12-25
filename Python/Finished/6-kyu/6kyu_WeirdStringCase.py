def to_weird_case(string):
    listStringWeird = []
    for word in string.split():
        StringWeird = ''
        for j, letter in enumerate(word):
            if j%2==0:
                StringWeird += letter.upper()
            else:
                StringWeird += letter.lower()

        listStringWeird.append(StringWeird)

    return ' '.join(listStringWeird)