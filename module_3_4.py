def single_root_words(root_word, *other_words):
    same_words = None
    if same_words is None:
        same_words = []
    for i in other_words:
        if len(root_word) < len(i):
            if root_word in i:
                same_words.append(i)
        else:
            if i.upper() in root_word.upper():
                same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)