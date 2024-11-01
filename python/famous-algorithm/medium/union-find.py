# https://www.algoexpert.io/questions/union-find


class UnionFind:
    def __init__(self):
        self.parents = {}

    # O(1) Time | O(1) Space
    def createSet(self, value):
        self.parents[value] = value

    # O(n) Time | O(1) Space
    def find(self, value):
        if value not in self.parents:
            return None
        while value != self.parents[value]:
            value = self.parents[value]

        return value

    # O(n) Time | O(1) Space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        self.parents[valueOneRoot] = valueTwoRoot