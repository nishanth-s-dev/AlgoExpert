# https://www.algoexpert.io/questions/union-find


class UnionFind:
    def __init__(self):
        self.parents = {}

    # O(1) Time | O(1) Space
    def createSet(self, value):
        if value not in self.parents:
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


class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) Time | O(1) Space
    def createSet(self, value):
        if value not in self.parents:
            self.parents[value] = value
            self.ranks[value] = 0

    # O(log n) Time | O(1) Space
    def find(self, value):
        if value not in self.parents:
            return None
        while value != self.parents[value]:
            value = self.parents[value]

        return value

    # O(log n) Time | O(1) Space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)

        valueOneRank = self.ranks[valueOne]
        valueTwoRank = self.ranks[valueTwo]

        if valueOneRank < valueTwoRank:
            self.parents[valueOneRoot] = valueTwoRoot
        elif valueOneRoot > valueTwoRoot:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.ranks[valueOneRoot] += 1


class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) Time | O(1) Space
    def createSet(self, value):
        if value not in self.parents:
            self.parents[value] = value
            self.ranks[value] = 0

    # O(1) Time | O(1) Space
    def find(self, value):
        if value not in self.parents:
            return None

        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])

        return self.parents[value]

    # O(1) Time | O(1) Space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)

        valueOneRank = self.ranks[valueOne]
        valueTwoRank = self.ranks[valueTwo]

        if valueOneRank < valueTwoRank:
            self.parents[valueOneRoot] = valueTwoRoot
        elif valueOneRoot > valueTwoRoot:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.ranks[valueOneRoot] += 1