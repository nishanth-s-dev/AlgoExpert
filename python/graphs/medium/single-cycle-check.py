# https://www.algoexpert.io/questions/single-cycle-check

def hasSingleCycle(array):
    array_length = len(array)
    no_of_visited_elements = 0
    current_index = 0

    while no_of_visited_elements < array_length:
        if current_index == 0 and no_of_visited_elements > 0:
            return False
        current_index = circular_index(current_index, array[current_index], array_length)
        no_of_visited_elements += 1

    return current_index == 0


def circular_index(current_index, offset, array_length):
    next_index = (current_index + offset) % array_length
    return next_index if next_index >= 0 else next_index + array_length

if __name__ == '__main__':
    print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
    print(hasSingleCycle([2, 2, 2]))
    print(hasSingleCycle([1, 1, 1, 1, 2]))
