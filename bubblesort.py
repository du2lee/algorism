def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index_2 in range(len(data) - index - 1):
            if data[index_2] > data[index_2 + 1]:
                data[index_2], data[index_2 + 1] = data[index_2 + 1], data[index_2]
                swap = True
        if swap == False:
            break
    return data