def find_min(root):
    while root.left:
        root = root.left
    return root.data


def find_max(root):
    while root.right:
        root = root.right
    return root.data


print("Minimum:", find_min(root))
print("Maximum:", find_max(root))