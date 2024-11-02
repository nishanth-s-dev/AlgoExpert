# https://www.algoexpert.io/questions/single-cycle-check

def hasSingleCycle(array):
    array_length = len(array)
    if not array:
        return False

    current_index = 0
    firstElement = array[current_index]
    lastElement = None

    for i in range(array_length):
        current_index = circular_index(current_index, array[i], array_length)
        lastElement = array[current_index]
        if lastElement == 0:
            break

    print(firstElement, lastElement)
    return current_index == 0



def circular_index(current_index, offset, array_length):
    return (current_index + offset + array_length) % array_length

if __name__ == '__main__':
    # print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
    # print(hasSingleCycle([2, 2, 2]))
    print(hasSingleCycle([1, 1, 1, 1, 2]))
