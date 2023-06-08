# O(n) time| O(n) space
from binaryTree import root

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
