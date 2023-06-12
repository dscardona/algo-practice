class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, child):
        self.children.append(child)

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

# Create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
nodeI = Node("I")

# Connect nodes
nodeA.addChild(nodeB)
nodeA.addChild(nodeC)
nodeA.addChild(nodeD)
nodeB.addChild(nodeE)
nodeB.addChild(nodeF)
nodeD.addChild(nodeG)
nodeD.addChild(nodeH)
nodeF.addChild(nodeI)

# Test the depthFirstSearch function
# Solution ['A', 'B', 'E', 'F', 'I', 'C', 'D', 'G', 'H']
result = nodeA.depthFirstSearch([])
print(result)
