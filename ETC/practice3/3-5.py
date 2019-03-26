def search(lists, li):
    for i in range(len(lists)):
        if li == lists[i]:
            return i
    return False
