def comp(a1, a2):
    count = 0
    if a1 == None or a2 == None:
        return False
    else:
        for i in a1:    
            if i*i in a2 and a1.count(i) == a2.count(i*i):
                count += 1
                
        return count == len(a2) 
