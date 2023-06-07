# O(n) time| O(n) space

# Create Node class to construct a binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Implement create binary tree function
def createBinaryTree():
    # Level 0
    root = Node(1)

    # Level 1
    root.left = Node(2)
    root.right = Node(3)

    # Level 2
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    return root

# Create binary tree
root = createBinaryTree()



def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

# Recursive function
def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
        
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)

print(branchSums(root))
