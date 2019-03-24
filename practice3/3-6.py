def search_char(words, word):
    for i in range(len(words)):
        if words[i] == word:
            return i
    return -1
