class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None

head = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))
    curr = Node(data)

    if head is None:
        head = curr
    else:
        ptr.next = curr  
    ptr = curr   

ptr = head
while ptr is not None:
    print(ptr.data, end=" [] ")
    ptr = ptr.next

print("NULL")