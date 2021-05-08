def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j] >= data[j - 1]:
                break
            data[j], data[j - 1] = data[j - 1], data[j]
    return data

