# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

# Create class
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

# Function that builds tree
def build_tree(data):
    node_dict = {node['id']: node for node in data['nodes']}
    root_id = data['root']
    root_node = node_dict[root_id]
    tree = BST(root_node['value'])

    def helper(node, node_data):
        if node_data['left']:
            left_node_data = node_dict[node_data['left']]
            node.left = BST(left_node_data['value'])
            helper(node.left, left_node_data)
        if node_data['right']:
            right_node_data = node_dict[node_data['right']]
            node.right = BST(right_node_data['value'])
            helper(node.right, right_node_data)

    helper(tree, root_node)
    return tree

# Date to build binary tree
data = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "13", "left": None, "right": "14", "value": 13},
        {"id": "14", "left": None, "right": None, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": None, "value": 2},
        {"id": "1", "left": None, "right": None, "value": 1}
    ],
    "root": "10"
}

# Instantiate tree
tree = build_tree(data)

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
print(findClosestValueInBst(tree, 12))