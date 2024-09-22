# Problem : https://www.algoexpert.io/questions/nth-fibonacci

def getNthFib(n):
    if n <= 2:
        return n - 1
    return getNthFib(n - 1) + getNthFib(n - 2)
