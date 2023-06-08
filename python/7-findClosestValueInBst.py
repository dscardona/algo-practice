# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

from binaryTree import root

# Function to find closest value calls helper function
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

# Helper function finds closest value recursively
def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

# Call function with tree instantiated above, closest num should be 13.
print(findClosestValueInBst(root, 12))