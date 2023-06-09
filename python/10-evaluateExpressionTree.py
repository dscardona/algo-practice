from expressionTree import root

# O(n) time | O(h) space
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue / rightValue)

    return leftValue * rightValue

print(evaluateExpressionTree(root))