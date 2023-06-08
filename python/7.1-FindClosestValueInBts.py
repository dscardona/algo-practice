# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

from binaryTree import root

# Function to run helper method
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

# Helper method is iterative, not recursive, see time/space complexity
def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

# Call function with tree instantiated above, closest num should be 13.
print(findClosestValueInBst(root, 12))