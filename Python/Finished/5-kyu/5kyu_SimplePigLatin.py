def pig_it(text):
    newText = []
    for word in text.split():
        if word.isalpha():
            newText.append(word[1:]+word[0]+'ay')
        else:
            newText.append(word)
        
    return ' '.join(newText)
