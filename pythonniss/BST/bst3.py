def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


key = int(input("\nEnter element to search: "))

if search(root, key):
    print("Element found")
else:
    print("Element not found")