def move_zeros(array):
    for i in array:
        if i == 0:
            array.append(array.pop(array.index(0)))

    return array