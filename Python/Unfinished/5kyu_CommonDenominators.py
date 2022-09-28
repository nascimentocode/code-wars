def convert_fracts(lst):
    for i in lst:
        lst[lst.index(i)] = [12//i[1], 12]
        
    return lst

print(convert_fracts([[1, 2], [1, 3], [1, 4]]))