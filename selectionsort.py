def selection_sort(data):
    for i in range(len(data) - 1):
        min = i
        for j in range(i + 1, len(data)):
            if data[min] > data[j]:
                min = j
        data[min] , data[i] = data[i], data[min]
    return data