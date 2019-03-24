def sort_scores(*scores):
    a_list = []
    for i in range(len(scores)):
        a_list.append(scores[i])
    a_list.sort(reverse=True)

    for i in a_list:
        print(i)
