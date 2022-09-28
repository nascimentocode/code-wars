def find_uniq(arr):
    arrSet = set(arr)
    for n in arrSet:
        if arr.count(n) == 1:
            return n