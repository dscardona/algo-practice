class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createExpressionTree():
    data = {
        "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": -1},
            {"id": "2", "left": None, "right": None, "value": 2},
            {"id": "3", "left": None, "right": None, "value": 3}
        ],
        "root": "1"
    }

    nodes = {}
    for node_data in data["nodes"]:
        node_id = node_data["id"]
        node = BinaryTree(node_data["value"])
        nodes[node_id] = node

    for node_data in data["nodes"]:
        node_id = node_data["id"]
        node = nodes[node_id]
        left_id = node_data["left"]
        right_id = node_data["right"]

        if left_id is not None:
            node.left = nodes[left_id]

        if right_id is not None:
            node.right = nodes[right_id]

    return nodes[data["root"]]


# expression tree solution: 5
root = createExpressionTree()