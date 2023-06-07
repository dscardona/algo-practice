# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

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

# Data to build binary tree
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
print(findClosestValueInBst(tree, 12))