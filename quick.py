import random

def quicksort(data):
    if len(data)<= 1:
        return data
    pivot = data[0]
    left = list(i for i in data[1:] if i < pivot)
    right = list(i for i in data[1:] if i > pivot)

    return quicksort(left) + [pivot] + quicksort(right)



data_list = random.sample(range(100), 10)       #example data

print(quicksort(data_list))                     #result