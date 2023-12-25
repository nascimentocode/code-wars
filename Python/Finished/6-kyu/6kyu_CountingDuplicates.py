def duplicate_count(text):
    lowerText = text.lower()
    result = []

    for i in lowerText:
        if lowerText.count(i) > 1: # Ou poderia ser assim → if lowerText.count(i) > 1 and i not in result:
            result.append(i)
    
    return len(set(result)) # Nem precisaria mais do set(result)
