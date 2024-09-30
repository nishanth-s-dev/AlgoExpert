# Problem : https://www.algoexpert.io/questions/breadth-first-search

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)

            currentName = current.name
            currentChildren = current.children

            array.append(currentName)

            for node in currentChildren:
                queue.append(node)
        return array