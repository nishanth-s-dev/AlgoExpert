def insertionSort(array):
    for i in range(len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array

print(insertionSort([5, 3, 2, 4, 1]))