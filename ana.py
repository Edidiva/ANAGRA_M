def find_anagram(word, anagram):
    X = word.lower()
    Y = anagram.lower()
    list_word = list(X)
    list_anagram = list(Y)
    Z = []
    for i in list_anagram:
        if i in list_word:
            list_word.remove(i)
            Z.append(i)  
    if result is True:
            print("This is an anagram")
            return True
    else:
        print("This is not an anagram")
        return False
print(find_anagram("EAT", "ATE"))
