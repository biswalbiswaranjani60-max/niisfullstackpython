# Binary Search Tree (BST) - Hello September

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# Create BST
root = None

words = ["Hello", "September"]

for word in words:
    root = insert(root, word)

print("🌸 BST Inorder Traversal:")
inorder(root)