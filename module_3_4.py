def single_root_words(root_word, *other_words):
    same_words = []
    for word in range(len(other_words)): # word равно 0, 1, 2 и тд - зависит от кол-ва слов
        i = other_words[word].lower()
        if i in root_word.lower() or root_word.lower() in i:
            same_words.append(other_words[word])
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)