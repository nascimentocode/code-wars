def anagrams(word, words):
    print(word)
    for i in word:
        print(i, "i")
        print(words)
        for j in words:
            print(j, "j")
            if len(j) != len(word):
                words.remove(j)
            else:
                if i not in j:
                    words.remove(j)
                elif word.count(i) != j.count(i):
                    words.remove(j)
    return words

print(anagrams('laser', ['lazing', 'lazy',  'lacer']))