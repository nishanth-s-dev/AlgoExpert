# https://www.algoexpert.io/questions/depth-first-search

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in array:
            child.depthFirstSearch(array)
        return array
