# Binary Search Tree (BST)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Search
def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Inorder: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main
root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input(f"Enter element {i + 1}: "))
    root = insert(root, data)


# Display
print("\nInorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)


# Search
key = int(input("\n\nEnter element to search: "))

if search(root, key):
    print(key, "is found in BST")
else:
    print(key, "is not found in BST")