def reverse_text(*words):
    n = 0
    for i in range(len(words)):
        if len(words[i]) % 2 == 0:
            print(words[i])
        else:
            print(words[i][::-1])
            n += 1
    return n
